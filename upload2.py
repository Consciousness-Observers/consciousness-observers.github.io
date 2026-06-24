#!/usr/bin/env python3
"""Upload updated CO-LAB files via Git Data API."""
import base64, json, os, subprocess

REPO = "Consciousness-Observers/consciousness-observers.github.io"
BASE = os.path.expanduser("~/colab-website")

FILES = [
    "_pages/home.md", "_pages/members.md", "_pages/projects.md",
    "_pages/seminars.md", "_pages/publications.md", "_pages/join.md",
    "_data/projects.yml"
]

def gh(method, endpoint, data=None):
    cmd = ['gh', 'api', '--method', method, f'repos/{REPO}/{endpoint}']
    if data:
        tmp = '/tmp/gh_colab_payload.json'
        json.dump(data, open(tmp, 'w'))
        cmd += ['--input', tmp]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        os.remove(tmp)
    else:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if r.returncode != 0:
        print(f"  FAIL: {r.stderr[:300]}")
        return None
    return json.loads(r.stdout)

# Get HEAD
r = subprocess.run(['gh', 'api', f'repos/{REPO}/git/ref/heads/main', '--jq', '.object.sha'],
                   capture_output=True, text=True, timeout=10)
HEAD = r.stdout.strip()
print(f"HEAD: {HEAD}")

trees = []
for rel in FILES:
    full = os.path.join(BASE, rel)
    content_b64 = base64.b64encode(open(full, 'rb').read()).decode('utf-8')
    blob = gh('POST', 'git/blobs', {'content': content_b64, 'encoding': 'base64'})
    if not blob: continue
    trees.append({'path': rel, 'mode': '100644', 'type': 'blob', 'sha': blob['sha']})
    print(f"  OK: {rel}")

tree = gh('POST', 'git/trees', {'base_tree': HEAD, 'tree': trees})
print(f"Tree: {tree['sha']}")

commit = gh('POST', 'git/commits', {
    'message': 'Rewrite pages: natural tone, fix encoding, remove duplicate home nav',
    'tree': tree['sha'],
    'parents': [HEAD]
})
print(f"Commit: {commit['sha']}")

gh('PATCH', 'git/refs/heads/main', {'sha': commit['sha'], 'force': False})
print("DONE")
