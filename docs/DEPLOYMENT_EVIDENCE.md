# Standing StudioNet deployment evidence

## Status

**BLOCKED — no value-bearing deployment was performed.** The source passed stable local verification, but the exact hosted GenVM/web runtime does not expose an effective redirect destination or a no-redirect restriction for `gl.nondet.web.render`. The initial hostname allowlist therefore cannot prove that fetched evidence remained on the approved authority. The deployment script exits with code 14 until this policy is verified or the evidence path is changed.

Observed during workspace execution on `2026-10-20`:

- Network name: `studionet`
- Chain ID: `61999`
- RPC: `https://studio.genlayer.com/api`
- Repository-local CLI: `genlayer@0.39.1`
- CLI network info: `Genlayer Studio Network`, chain ID `61999`, RPC above
- Independent RPC method: `eth_chainId`
- Independent RPC result: `0xf22f`, parsed as decimal `61999`
- Explorer base configured by the CLI: `https://genlayer-explorer.vercel.app`

## Local verification evidence

- Python: `3.12.10` virtual environment
- Offline suite: **39 passed**
- Direct Mode: **12 passed**, `genlayer-test==0.29.0`; web and LLM observations are mocked
- GenVM linter: `genvm-linter==0.11.0`
- Stable GenVM artifact selected: `v0.2.12`
- `contracts/standing.py`: stable `check` passed; 13 methods, 6 views, 7 writes, no constructor parameters
- `contracts/protected_challenge.py`: stable `check` passed; 3 methods, 2 views, 1 write, 3 constructor parameters
- Schema extraction: passed for both deployable contracts under `GENVM_VERSION=v0.2.12`
- Python compilation: passed for `contracts`, `tests`, and `scripts`
- Static preflight: passed, including local CLI pin, npm lockfile, CI stable-artifact pin and deployment guard

## Source identity

- Final Git commit: recorded in the final handoff after commit/push
- `contracts/standing.py` SHA-256: recorded in `SOURCE_SHA256_MANIFEST.json` after final source freeze
- `contracts/protected_challenge.py` SHA-256: recorded in `SOURCE_SHA256_MANIFEST.json` after final source freeze

## Deployment records

### Standing

- Address: **NOT DEPLOYED — blocked by redirect policy**
- Deployment transaction: **NONE**
- Finalized execution: **NOT APPLICABLE**
- Explorer URL: **NONE**
- Source-matched receipt: **NONE**

### ProtectedChallenge

- Address: **NOT DEPLOYED — Standing was not finalized**
- Deployment transaction: **NONE**
- Finalized execution: **NOT APPLICABLE**
- Explorer URL: **NONE**
- Constructor Standing address: **NOT APPLICABLE**

## Live lifecycle records

No live charter, matter, petition, consumer, expiry, closure or replay transaction is claimed. Direct Mode cases are explicitly mock-based and are not live StudioNet evidence.

## Required corrective action

Before deployment, verify on the stable hosted runtime that same-host redirects are constrained to the approved effective host and cross-host, attacker-host, internal-host, encoded-URL and user-information cases fail closed. If the runtime cannot expose that guarantee, replace the web evidence primitive or disable the value-bearing public positive path, then rerun the security and deployment gates.
