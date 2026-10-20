"""Static guard against accidental preview-chain deployments or global CLI calls."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
pkg=json.loads((ROOT/'package.json').read_text())
assert pkg['devDependencies']['genlayer']=='0.39.1'
assert (ROOT/'package-lock.json').is_file()
deploy=(ROOT/'scripts/deploy_studionet.sh').read_text()
assert "./node_modules/.bin/genlayer" in deploy
assert "network set studionet" in deploy
assert "https://studio.genlayer.com/api" in deploy
assert "scripts/verify_studionet.py" in deploy
assert "scripts/verify_authenticated_evidence.py" in deploy
assert ' deploy --contract contracts/standing.py\n' in deploy
assert ' --rpc ' not in deploy
assert "AUTHENTICATED_EVIDENCE_STATUS=VERIFIED" in deploy
assert "REDIRECT_POLICY_STATUS" not in deploy
assert 'exit 14' in deploy
checks=(ROOT/'scripts/verify_studionet.py').read_text()
assert '61999' in checks and 'raise RuntimeError' in checks
assert "'User-Agent': 'standing-studionet-guard/1.0'" in checks
auth=(ROOT/'scripts/verify_authenticated_evidence.py').read_text()
for marker in ['class EvidenceCommitment', 'commit_evidence_hash',
               'keccak(source) != expected_evidence_hash',
               'AUTHENTICATED_EVIDENCE_STATUS=VERIFIED']:
    assert marker in auth
ci=(ROOT/'.github/workflows/ci.yml').read_text()
assert 'npm ci --no-audit --no-fund' in ci
assert 'GENVM_VERSION: v0.2.12' in ci
for path in [ROOT/'contracts/standing.py',ROOT/'contracts/protected_challenge.py']:
    assert 'gl.Contract' in path.read_text()
print('PASS: repo-local CLI pin 0.39.1, RPC and 61999 deployment hard gates')
