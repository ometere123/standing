# Reviewer guide — Standing Intelligent Contract

## Single sentence

Standing makes the right to initiate a costly challenge a consensus-verifiable, scope-limited, time-bound right, while leaving the underlying merits entirely to a separate adjudicator.

## Why GenLayer is necessary

A wallet's relationship to a publicly described matter cannot be derived deterministically from arbitrary external wording. The narrow public-material-interest decision is therefore placed inside a GenLayer nondeterministic block: a leader evaluates both frozen sources, and validators independently fetch and evaluate both sources before accepting bounded verdicts and source-grounded quotes. Known direct parties are registered deterministically and never require AI.

## Correctness invariant

`is_eligible(matter_id, frozen_hash, wallet)` returns true only while the matter is active and unexpired, the supplied hash equals the activated matter hash, and either a frozen registered grant matches the wallet or the latest wallet-submitted public petition passed both source checks and remains valid. The consumer additionally pins the intended matter at construction and passes the actual caller address to the typed Standing view.

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
```

On Windows PowerShell, set `$env:GENVM_VERSION='v0.2.12'` before the Python/linter commands and use `\.\node_modules\.bin\genlayer.cmd`. The Direct Mode suite currently records 12 passed tests; the offline suite records 39 passed tests. Direct Mode web and LLM observations are mocks, so they must not be presented as live StudioNet consensus.

## Security cases covered

- sealed charter and activated matter immutability;
- typed address registration, role validation, duplicates, controller checks and lifetime bounds;
- exact matter-hash and cross-matter binding;
- wallet-bound public petitions, two-source requirement, unavailable/ambiguous/unsupported evidence, malformed model output, attempt limits, latest-petition replacement and expiry;
- hostile leader quote/verdict disagreement and prompt-injection-resistant evidence framing;
- one-use consumer challenge keys and constructor-pinned protected matter.

## Deployment status

The chain guard independently confirmed `studionet`, chain `61999`, RPC `https://studio.genlayer.com/api`, and local CLI `0.39.1`. No contract was deployed in this revision. The deployment script intentionally stops because stable `gl.nondet.web.render` exposes no effective redirect destination or no-redirect control. The GenVM webdriver follows navigation from the requested URL and returns content/status without an effective-host assertion ([web access](https://docs.genlayer.com/developers/intelligent-contracts/features/web-access), [webdriver source](https://github.com/genlayerlabs/genvm/blob/main/modules/webdriver/src/prj/src/index.ts)). A hostname check on the initial URL is therefore not sufficient for value-bearing public standing. This is an explicit blocker, not missing evidence to be filled with a guessed address.

## Source discipline

Only new, finalized 61999 transactions for the exact committed source may be added to `docs/DEPLOYMENT_EVIDENCE.md`. Until redirect safety is resolved, deployment addresses, transaction hashes, explorer links and live lifecycle claims remain explicitly unresolved.
