#!/usr/bin/env python3
"""Push personal homepage changes via Git Data API."""
import base64, json, os, subprocess

REPO = "psychwangzihao/psychwangzihao.github.io"
BASE = os.path.expanduser("~/personal-homepage")

def gh(method, endpoint, data=None):
    cmd = ['gh', 'api', '--method', method, f'repos/{REPO}/{endpoint}']
    if data:
        tmp = '/tmp/gh_pp_payload.json'
        json.dump(data, open(tmp, 'w'))
        cmd += ['--input', tmp]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        os.remove(tmp)
    else:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        print(f"  FAIL: {result.stderr[:300]}")
        return None
    return json.loads(result.stdout)

# Get current HEAD
head_r = subprocess.run(['gh', 'api', f'repos/{REPO}/git/ref/heads/main', '--jq', '.object.sha'],
                        capture_output=True, text=True, timeout=10)
HEAD = head_r.stdout.strip()
print(f"Remote HEAD: {HEAD}")

# Only upload changed files (remote HEAD -> local HEAD)
changed = subprocess.run(
    ['git', '-C', BASE, 'diff', '--name-only', f'{HEAD}..d876c87'],
    capture_output=True, text=True
)
files = [f.strip() for f in changed.stdout.strip().split('\n') if f.strip()]
print(f"Changed files: {files}")

# Upload each changed file
trees = []
for rel in files:
    full = os.path.join(BASE, rel)
    if not os.path.exists(full):
        print(f"  SKIP (deleted): {rel}")
        continue
    content_b64 = base64.b64encode(open(full, 'rb').read()).decode('utf-8')
    blob = gh('POST', 'git/blobs', {'content': content_b64, 'encoding': 'base64'})
    if not blob:
        print(f"  BLOB FAIL: {rel}")
        continue
    trees.append({'path': rel, 'mode': '100644', 'type': 'blob', 'sha': blob['sha']})
    print(f"  OK: {rel}")

# Create tree
tree = gh('POST', 'git/trees', {'base_tree': HEAD, 'tree': trees})
print(f"Tree: {tree['sha']}")

# Create commit
commit = gh('POST', 'git/commits', {
    'message': 'Redirect Group page to CO-LAB website',
    'tree': tree['sha'],
    'parents': [HEAD]
})
print(f"Commit: {commit['sha']}")

# Update ref
gh('PATCH', 'git/refs/heads/main', {'sha': commit['sha'], 'force': False})
print("DONE")
