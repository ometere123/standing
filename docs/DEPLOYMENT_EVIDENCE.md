# Standing StudioNet deployment evidence

## Status

**PENDING — no value-bearing deployment has been performed in this revision.** The exact stable v0.2.12 runtime does not expose an effective redirect destination or a no-redirect restriction. Standing therefore authenticates exact rendered bytes against two immutable, sender-authenticated authority commitments before any semantic grant. Changed redirected content fails the commitment check; identical committed bytes do not create a new authorization. The deployment script exits with code 14 unless the derived authenticated-evidence proof gate passes.

Observed during workspace execution on `2026-10-20`:

- Network name: `studionet`
- Chain ID: `61999`
- RPC: `https://studio.genlayer.com/api`
- Repository-local CLI: `genlayer@0.39.1`
- CLI network info: `Genlayer Studio Network`, chain ID `61999`, RPC above
- Independent RPC method: `eth_chainId`
- Independent RPC result: `0xf22f`, parsed as decimal `61999`
- Explorer base configured by the CLI: `https://genlayer-explorer.vercel.app`
- Authenticated evidence gate: `scripts/verify_authenticated_evidence.py` emitted `AUTHENTICATED_EVIDENCE_STATUS=VERIFIED` after source checks and targeted stable Direct Mode regressions.

## Local verification evidence

- Python: `3.12.10` virtual environment
- Offline suite: **43 passed**
- Direct Mode: **16 passed**, `genlayer-test==0.29.0`; web and LLM observations are mocked
- GenVM linter: `genvm-linter==0.11.0`
- Stable GenVM artifact selected: `v0.2.12`
- `contracts/standing.py`: stable `check` passed; 15 methods, 7 views, 8 writes, no constructor parameters
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

- Address: **PENDING — not yet deployed**
- Deployment transaction: **NONE**
- Finalized execution: **NOT APPLICABLE**
- Explorer URL: **NONE**
- Source-matched receipt: **NONE**

### ProtectedChallenge

- Address: **PENDING — Standing not yet finalized**
- Deployment transaction: **NONE**
- Finalized execution: **NOT APPLICABLE**
- Explorer URL: **NONE**
- Constructor Standing address: **NOT APPLICABLE**

## Live lifecycle records

No live charter, matter, petition, consumer, expiry, closure or replay transaction is claimed. Direct Mode cases are explicitly mock-based and are not live StudioNet evidence.

## Required corrective action

Complete the stable StudioNet deployment after the authenticated-evidence gate, record both finalized successful receipts and source-matched hashes, then run the live lifecycle using authentic authority commitments and publicly verifiable evidence. Direct Mode mock results must remain clearly separated from live consensus receipts.
