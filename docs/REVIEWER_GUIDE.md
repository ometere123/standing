# Reviewer guide — Standing Intelligent Contract

## Single sentence

Standing makes the right to initiate a costly challenge a consensus-verifiable, scope-limited, time-bound right, while leaving the underlying merits entirely to a separate adjudicator.

## Why GenLayer is necessary

A wallet's relationship to a publicly described matter cannot be derived deterministically from arbitrary external wording. The narrow public-material-interest decision is therefore placed inside a GenLayer nondeterministic block: two distinct authority principals first commit exact evidence hashes for the claimant/matter/source tuple, then a leader fetches and evaluates both records, and validators independently fetch, hash-check and evaluate both records before accepting bounded verdicts and source-grounded quotes. Known direct parties are registered deterministically and never require AI. The hash commitment is the redirect-safe authenticity boundary; the model remains responsible for the semantic material-interest assessment.

## Correctness invariant

`is_eligible(matter_id, frozen_hash, wallet)` returns true only while the matter is active and unexpired, the supplied hash equals the activated matter hash, and either a frozen registered grant matches the wallet or the latest wallet-submitted public petition passed both authenticated source checks and remains valid. The consumer additionally pins the intended matter at construction and passes the actual caller address to the typed Standing view.

## Reproduction

From the repository root, install Python 3.12+, Node LTS, and the committed dependencies:

```bash
python -m pip install -r requirements.txt
GENVM_VERSION=v0.2.12 python -m pytest tests/offline -q
GENVM_VERSION=v0.2.12 python -m pytest -p no:gltest -p gltest_direct tests/direct -v
GENVM_VERSION=v0.2.12 genvm-lint check contracts/standing.py --json
GENVM_VERSION=v0.2.12 genvm-lint check contracts/protected_challenge.py --json
genvm-lint schema contracts/standing.py --json
genvm-lint schema contracts/protected_challenge.py --json
npm ci
./node_modules/.bin/genlayer --version
python scripts/verify_studionet.py
python scripts/verify_authenticated_evidence.py
```

On Windows PowerShell, set `$env:GENVM_VERSION='v0.2.12'` before the Python/linter commands and use the repository-local `node_modules/.bin/genlayer.cmd`. The Direct Mode suite currently records 16 passed tests; the offline suite records 43 passed tests. Direct Mode web and LLM observations are mocks, so they must not be presented as live StudioNet consensus.

## Security cases covered

- sealed charter and activated matter immutability;
- two distinct authority principals, immutable matter-bound evidence commitments and sender authentication;
- typed address registration, role validation, duplicates, controller checks and lifetime bounds;
- exact matter-hash and cross-matter binding;
- wallet-bound public petitions, two-source requirement, unavailable/ambiguous/unsupported evidence, malformed model output, attempt limits, latest-petition replacement and expiry;
- hostile leader quote/verdict disagreement and prompt-injection-resistant evidence framing;
- redirect substitution, invalid commitment, forged authority, wrong wallet/matter and oversized-source rejection;
- one-use consumer challenge keys and constructor-pinned protected matter.

## Deployment status

The chain guard independently confirmed `studionet`, chain `61999`, RPC `https://studio.genlayer.com/api`, and local CLI `0.39.1`. Stable `gl.nondet.web.render` does not expose an effective redirect destination, so the contract authenticates exact rendered bytes against immutable authority commitments. The deployment script runs `scripts/verify_authenticated_evidence.py`, which executes the hash/redirect regressions and fails closed if they do not pass.

Standing is finalized at [`0x5b27dB099296AAF72f7F36f458cbdD79B9f64d4f`](https://explorer-studio.genlayer.com/address/0x5b27dB099296AAF72f7F36f458cbdD79B9f64d4f). The direct-party consumer is [`0xb894c8769f38Ee4685Edc26710edB3D0c12F7bB0`](https://explorer-studio.genlayer.com/address/0xb894c8769f38Ee4685Edc26710edB3D0c12F7bB0), and the public-interest consumer is [`0x28AbC74d187F8c8dA258e8d4f6267cFE4DFb60b2`](https://explorer-studio.genlayer.com/address/0x28AbC74d187F8c8dA258e8d4f6267cFE4DFb60b2). All three deployment receipts are finalized with execution success and source-matched hashes.

The live record includes a registered-party success, wrong-wallet/replay/closure failures, a genuine validator disagreement, a fail-closed ambiguous quote, a successful authenticated public petition with two supported sources, a missing-commitment denial, and a successful typed public consumer challenge. The one-hour live expiry wait was not claimed; Direct Mode covers expiry.

## Source discipline

Only new, finalized 61999 transactions for the exact committed source may be added to `docs/DEPLOYMENT_EVIDENCE.md`. Direct Mode and mocked web responses are not live consensus evidence. Authority commitment principals and public evidence must be authentic; related hostnames must not be described as institutionally independent without proof.
