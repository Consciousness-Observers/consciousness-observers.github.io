#!/usr/bin/env python3
"""Upload CO-LAB files as a single git commit via Git Data API."""
import base64, json, os, subprocess, sys

REPO = "Consciousness-Observers/consciousness-observers.github.io"
BASE = os.path.dirname(os.path.abspath(__file__))
# Get current HEAD from remote
import subprocess as sp
head_result = sp.run(['gh', 'api', f'repos/{REPO}/git/ref/heads/main', '--jq', '.object.sha'],
                     capture_output=True, text=True, timeout=10)
HEAD = head_result.stdout.strip()
print(f"Current HEAD: {HEAD}")

def gh(method, endpoint, data=None):
    """Run gh api and return parsed JSON."""
    cmd = ['gh', 'api', '--method', method, f'repos/{REPO}/{endpoint}']
    if data:
        tmp = '/tmp/gh_payload.json'
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

print("Step 1: Creating blobs...")
trees = []
files_uploaded = 0
for root, dirs, files in os.walk(BASE):
    parts = root.split(os.sep)
    if '.git' in parts or '_site' in root or '.jekyll-cache' in root:
        continue
    # Only upload .github files this time
    if '.github' not in parts:
        continue
    for f in files:
        if f in ('.DS_Store', 'upload.py', 'README.md'):
            continue
        full = os.path.join(root, f)
        rel = os.path.relpath(full, BASE)
        size = os.path.getsize(full)

        if size > 5_000_000:
            print(f"  SKIP (>5MB): {rel}")
            continue

        content_b64 = base64.b64encode(open(full, 'rb').read()).decode('utf-8')

        # Create blob
        blob_data = {
            'content': content_b64,
            'encoding': 'base64'
        }
        blob = gh('POST', 'git/blobs', blob_data)
        if not blob:
            print(f"  BLOB FAIL: {rel}")
            continue

        trees.append({
            'path': rel,
            'mode': '100644',
            'type': 'blob',
            'sha': blob['sha']
        })
        files_uploaded += 1
        if files_uploaded % 20 == 0:
            print(f"  {files_uploaded} blobs created...")

print(f"  Total: {files_uploaded} blobs")

print("\nStep 2: Creating tree...")
tree_data = {
    'base_tree': HEAD,
    'tree': trees
}
tree = gh('POST', 'git/trees', tree_data)
if not tree:
    print("TREE FAIL")
    sys.exit(1)
print(f"  Tree SHA: {tree['sha']}")

print("\nStep 3: Creating commit...")
commit_data = {
    'message': 'CO-LAB website: Consciousness Observers platform\n\n'
               '- Home page with logo, vision, and mission\n'
               '- Members (equal, no hierarchy)\n'
               '- Projects: courses, workshops, outreach\n'
               '- Seminars: public transcripts\n'
               '- Publications: members\' papers\n'
               '- Join: admission process and norms',
    'tree': tree['sha'],
    'parents': [HEAD]
}
commit = gh('POST', 'git/commits', commit_data)
if not commit:
    print("COMMIT FAIL")
    sys.exit(1)
print(f"  Commit SHA: {commit['sha']}")

print("\nStep 4: Updating ref...")
ref_data = {
    'sha': commit['sha'],
    'force': False
}
ref = gh('PATCH', 'git/refs/heads/main', ref_data)
if ref:
    print(f"  SUCCESS: main -> {commit['sha']}")
else:
    print("REF UPDATE FAIL")
