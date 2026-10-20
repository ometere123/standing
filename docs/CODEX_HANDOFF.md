# CODEX: Final Standing engineering and StudioNet closeout

Repository: https://github.com/ometere123/standing

This is an existing **contract-only** project. Finish it in place. **Do not create a frontend, rewrite as a full app, switch networks, clone it into a different repository, or silently change the specification.**

## Hard environment lock

- Stable GenLayer network: **`studionet`**
- Chain ID: **`61999`**
- RPC: **`https://studio.genlayer.com/api`**
- Repository-local GenLayer CLI: **`genlayer@0.39.1`** exactly
- Global installed CLI `genlayer@0.40.0rc2` MUST NOT be invoked.
- **NEVER** `studio-dev`, `studionet-dev`, or chain `61997`.
- Contract-only: no UI, backend, storage service, paid third-party API, or Vercel.

## Mandatory execution sequence

1. Read README, SECURITY threat model, reviewer guide, contract source, tests and deployment evidence template. Work on repository `main` or a new feature branch with PR. Preserve git history.
2. Install Python >=3.12 and tools. Use pinned `genlayer-test==0.29.0` and the stable GenVM v0.2.12 direct runner; use pinned `genvm-linter==0.11.0` targeting stable GenVM v0.2.12; do NOT use preview-only RC tooling. Avoid the RC SDK lines intended only for 61997; verify protocol compatibility by documented evidence rather than assumption. Install the local CLI with `npm install --save-exact genlayer@0.39.1`. Commit **real** package-lock.json from registry. Use `npm ci` and `./node_modules/.bin/genlayer`, NEVER global CLI.
3. Run `python -m pytest tests/offline -q`; install GenLayer Direct Mode tools and run `python -m pytest -p no:gltest -p gltest_direct tests/direct -v`. If a mocked runtime fixture differs from documented current APIs, adapt tests faithfully—do not remove assertion scope or fake pass counts. Extend tests for public petition positive/negative results, malformed evidence, control injection, duplicate petitions, cross-matter replay, expiry, controller mutation and consumer gating. Keep real evidence separate from mocks.
4. Run GenVM linter and contract ABI/schema checks on both ICs, inspect warnings. Validate `run_nondet_default` custom leader/validator semantics and storage type compatibility. Ensure no unsafe default equality validator is used to “validate” semantic judgement.
5. **IMPORTANT**: establish the effective web redirect policy for `gl.nondet.web.render`; verify a 30x to a different host is rejected, or harden source fetching with a supported primitive that exposes effective URL/redirect controls. If the hosted runtime cannot enforce host policy, record this as a blocker for live value-bearing positive public standing. Do not claim two pinned authorities while silently accepting arbitrary off-domain redirects.
6. Inspect agent tests and deployment scripts for exact network values. `./node_modules/.bin/genlayer --version` must display `0.39.1`; `network set studionet`; verify chain ID `61999` from RPC or documented Studio API. On mismatch/unknown, STOP. No deploying under 61997.
7. Deploy primary IC to stable RPC; track to finalized successful status. Retrieve code or source and compare its hash to the exact commit. Deploy ProtectedChallenge referencing the finalized primary address, then likewise verify finalized success.
8. Run real lifecycle across immutable fixture sources, original claimant wallet and unrelated wallet, positive dual-source public case, negative case, stale/close case, and consumer replay case. Use **separately owned legitimate public fixture authorities**, avoiding redirects and account forgery. Do not issue fake public evidence. For adversarial leader divergence, prefer Direct Mode trace and label it mocked; do not present mocks as StudioNet consensus.
9. Fill `docs/DEPLOYMENT_EVIDENCE.md` with only actual source-matched, finalized address, hashes, receipt URLs, CI runs, test counts and statuses. Link explorer URLs, not merely RPC identifiers.
10. Commit/push all changes, ensure CI pass, and provide a concise submitter report: commit SHA, repository URL, network confirmation, exact CLI version, Standing/consumer addresses, explorer links, test counts, outstanding limitations, reviewer-blocker status. Never assert success if any check is incomplete.

## Threat model priorities

- Source host spoofing and redirects
- Web prompt injection; source text never instructions
- Literal wallet/ref anchors, issuer trust and spoofed wallet text
- Dual-source actually independent observation with substantive validator checks
- Immutable charter/matter definition and frozen grants
- Unauthorized caller / wrong matter hash / closed matter / expired public petition
- Attempt-limit gaming and replay of a challenge key
- Distinguish issuer-registered standing from consensus-adjudicated public standing
- Strictly fail-closed on unavailable or ambiguous evidence

If you find a legitimate defect, fix it with regression tests and document it. Do not paper over limitations with unsupported deployment claims.

## Current execution result (2026-10-20)

The final local stable gates completed: 43 offline checks, 16 Direct Mode checks with the v0.2.12 artifact selector, stable linter/schema checks for both contracts, repository-local CLI `0.39.1`, and independent RPC confirmation of chain `61999`. The exact v0.2.12 `gl.nondet.web.render` path does not expose an effective redirect destination or no-redirect restriction. The implementation uses a stable-compatible authenticated-evidence path: two distinct authority principals immutably precommit exact rendered-content hashes for each claimant/matter/source tuple; both leader and validator independently hash-check before semantic assessment. Standing and two ProtectedChallenge instances are finalized on stable StudioNet; the live evidence and source-matched receipts are in `docs/DEPLOYMENT_EVIDENCE.md`.

## Current continuation (2026-10-20)

- Implemented `EvidenceCommitment` storage, authority-principal checks, one-time commitment writes, commitment views, matter-hash binding, and fail-closed petition handling.
- Stable v0.2.12 supports `Keccak256` but exposes no contract-level ECDSA/secp256k1 verification primitive in the exact SDK bundle inspected. The selected precommitted-hash mechanism therefore uses only stable runtime functionality and preserves independent GenLayer semantic assessment.
- Expanded verification: **43 offline** checks and **16 stable Direct Mode** checks pass; the latter remain mock-based and are not live consensus evidence.
- Added `scripts/verify_authenticated_evidence.py`; it executes the hash/redirect regressions and emits `AUTHENTICATED_EVIDENCE_STATUS=VERIFIED` only after source checks and tests pass. The deployment script consumes this derived result and has no manually editable redirect bypass.
- Deployment, final source hashes and live lifecycle transactions are recorded in `docs/DEPLOYMENT_EVIDENCE.md`; the remaining documented limitation is that a one-hour live expiry wait was not claimed in this session.
