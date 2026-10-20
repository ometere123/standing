# Standing — who is entitled to challenge?

**Contract-only GenLayer primitive.** No frontend, application server, database, hosted dashboard, wallet UI, or Docker requirement.

Standing establishes *procedural eligibility*, not truth, guilt, compensation, or the merits of a challenge. It separates immutable matter-defined party roles from carefully bounded, independently corroborated **public material-interest petitions**. A second Intelligent Contract demonstrates genuine consumer-side gating.

> Neutral shared state is valuable here because the party trying to file a costly challenge cannot unilaterally decide its own standing. An owner may define a matter and source policy in advance, but may not rewrite those rules after activation or manufacture a public petition verdict after the fact.

## Exactly which network?

| Parameter | Value |
|---|---|
| Network name | `studionet` |
| Chain ID | `61999` |
| RPC | `https://studio.genlayer.com/api` |
| CLI package | **repo-local** `genlayer@0.39.1` |
| Forbidden | `studio-dev`, `studionet-dev`, chain `61997`, global `genlayer@0.40.0rc2` |

**Never substitute 61997 for 61999.** The pinned CLI is specified in `package.json`, the genuine `package-lock.json` is committed, and scripts reference `./node_modules/.bin/genlayer`, not a globally installed binary. Reproduce the JavaScript environment with `npm ci`.

## The protocol invariant

1. A charter owner defines a bounded public-interest test, permitted petition mode and lifetime. Once sealed, the charter's hash and policy never change.
2. A matter controller creates a **draft** referencing that charter, chooses two distinct public authority hostnames and two distinct, nonzero authority principals, and registers the exactly known direct parties/dependent consumers. An actor cannot be added after activation.
3. Activation freezes all relevant terms and registered actors in a canonical `matter_hash`.
4. Registered actors get standing *deterministically*; they do not require AI. Other wallets may petition on their **own sender address** only, and only if public petitions are enabled.
5. Before a public petition can be assessed, authority A and authority B each submit one immutable Keccak-256 commitment for the exact `(matter_id, frozen matter hash, claimant wallet, source)` tuple. The claimant supplies HTTPS URLs on the two frozen hosts, but URLs are distribution hints rather than authenticity proofs.
6. The leader fetches and hash-authenticates **both** committed records, then assesses the material-interest criterion. Validators independently fetch, hash-check and assess **both** records. A supporting quote must be literally present in the independently retrieved, committed bytes and contain both anchors. Disagreement means no safe finalization.
7. A public grant is short lived (max 72h) and cannot outlive the matter. Denied/ambiguous/unavailable evidence never creates standing.
8. The consumer verifies `(matter_id, expected_matter_hash, caller)` through the typed Standing interface before recording a one-use challenge key.

### Why isn't this “anyone can sue anyone”?

Matter owners set procedural scope up front; they **do not** get a blank check to insert eligible wallets once the matter is active. Public claimants can propose evidence but cannot confer eligibility on themselves, and the consumer cannot be fooled by a hash from a different matter version.

### Essential trust boundaries

- This primitive establishes only **standing under a configured charter**, **not legal standing in any court**.
- The matter controller selects the two source domains. Their institutional authority is a **controller-provided policy assumption**. The contract does not prove source authority or guaranteed independence.
- The matter controller selects two authority principals. Their authority to attest to a claimant's evidence is a **controller-provided trust assumption**. Each principal is authenticated by the transaction sender, and the commitment is immutable for the matter lifetime; two principals do not cryptographically prove institutional independence.
- Two different hostnames do not cryptographically guarantee two independent authors. To reduce accidental same-operator sources, sibling domains with a matching final two labels are rejected; sophisticated shared-control relationships remain an external trust limitation.
- Public evidence must explicitly connect a hexadecimal wallet to the matter: a human name alone cannot prove wallet ownership. Petition submission establishes control of `msg.sender`, but the public record must independently make the link.
- A matter controller may close the matter, which immediately disables future eligibility. This deliberate power is documented; use independent contract governance as the controller if a stronger liveness guarantee is needed.
- The URL checker prevents direct unsafe hostnames, encoded URLs and non-HTTPS links. Stable v0.2.12 does follow redirects without exposing the effective host, so host checks alone are not treated as authentication. The immutable content commitment is the security boundary: changed or attacker-substituted bytes fail the Keccak check before the model runs. Redirects can still cause unavailability, and the configured hosts remain an availability/distribution policy assumption.
- The `gl.nondet.web.render` mechanism is deliberately non-deterministic; disagreement (including changing web content) is a consensus failure, not something a client should paper over by accepting the leader alone.

## Files

- `contracts/standing.py` — one deployable authoritative Standing IC.
- `contracts/protected_challenge.py` — a separate consumer demonstrating *real* typed cross-IC reads.
- `tests/offline/` — deterministic guards and custom-validator pure-function checks, runnable without the SDK.
- `tests/direct/` — GenLayer Direct Mode tests to run once `genlayer-test` is available.
- `docs/THREAT_MODEL.md` — exact assumptions, known limitations, abuse tests.
- `docs/REVIEWER_GUIDE.md` — scoring rationale, setup, multi-path live cases.
- `docs/DEPLOYMENT_EVIDENCE.md` — source-matched finalized receipts and lifecycle links.
- `docs/live_evidence_record.md` and `docs/live_evidence_record_compact.md` — public reproducibility fixtures used by the live authenticated-evidence proof.
- `SUBMISSION.md` — submission-ready description and verified deployment fields.
- `scripts/` — preflight and deployment scripts hardlocked to stable StudioNet.
- `scripts/verify_authenticated_evidence.py` — derived fail-closed proof gate for the authority-commitment and redirect-substitution regressions.

## Run tests

Python 3.12+ and Node 18+ are recommended. Stable Direct Mode targets GenVM v0.2.12, NOT v0.6 preview. The implementation was syntax-checked with Python 3.13 in the authoring container.

```bash
python -m pytest tests/offline -q
python -m pip install -r requirements.txt
GENVM_VERSION=v0.2.12 python -m pytest -p no:gltest -p gltest_direct tests/direct -v
GENVM_VERSION=v0.2.12 genvm-lint check contracts/standing.py --json
GENVM_VERSION=v0.2.12 genvm-lint check contracts/protected_challenge.py --json
```

On Windows PowerShell, set `$env:GENVM_VERSION='v0.2.12'` for the Direct Mode and linter commands. The checked-in Direct Mode fixture also pins its cached artifact selector to v0.2.12.

Do not confuse successful offline tests with GenLayer Direct Mode or a finalized network consensus test. CI includes separate jobs for the two suites.

```bash
npm ci
./node_modules/.bin/genlayer --version
./node_modules/.bin/genlayer network set studionet
./node_modules/.bin/genlayer network info
```

The root `package.json` and committed lockfile pin `genlayer@0.39.1` exactly. Do not use the globally installed CLI.

## Deploy on StudioNet only

The deploy script validates local version, network selection, an RPC chain-ID proof, and the executed authenticated-evidence security gate. It **fails closed if it cannot prove 61999 or the hash-authentication regressions do not pass**. It does not modify wallet keys or search for credentials.

```bash
bash scripts/deploy_studionet.sh
```

The exact v0.2.12 source audit is recorded in `docs/THREAT_MODEL.md`: the runtime does not expose an effective host, so the contract authenticates the exact content instead. No redirect-based positive grant is accepted unless it serves the authority-precommitted bytes.

Expected stable RPC: `https://studio.genlayer.com/api`, not `https://studio-dev.genlayer.com/api`.

The final stable StudioNet deployment is recorded in `docs/DEPLOYMENT_EVIDENCE.md`: Standing is `0x5b27dB099296AAF72f7F36f458cbdD79B9f64d4f`, with finalized source-matched deployment transaction [0x3ea2…](https://explorer-studio.genlayer.com/tx/0x3ea2eab1c2f77421a75fad7ce16cc2ac96e29fe9e55096e672a6bb31dc439ce8), and ProtectedChallenge consumers are `0xb894c8769f38Ee4685Edc26710edB3D0c12F7bB0`, `0x28AbC74d187F8c8dA258e8d4f6267cFE4DFb60b2` and `0xBea9ac6AB160418FA59d602A944df01d938EB05E`. All consumer deployments pin the actual Standing address and a frozen matter hash.

See `docs/CODEX_HANDOFF.md` for the final exact agent instructions.

## Integration

```python
@gl.contract_interface
class IStanding:
    class View:
        def is_eligible(self, matter_id: u256, expected_matter_hash: str, claimant: Address) -> bool: ...
    class Write:
        pass

standing = IStanding(STANDING_ADDRESS)
assert standing.view().is_eligible(matter_id, stored_matter_hash, gl.message.sender_address)
```

The caller must freeze `expected_matter_hash` and *never* substitute a mutable caller-provided hash into security-sensitive contexts without checking it against its own intended matter. The bundled consumer demonstrates the typed call and one-time challenge-key replay protection, but an application must add its own challenge-handling logic and any fees/bonds.

## Live proof

The finalized live records include deterministic registered-party authorization, wrong-wallet and replay rollbacks, closed-matter rejection, an authenticated two-source public petition, a typed public-claimant consumer challenge, and a real one-hour expiry followed by `is_eligible=false` and a post-expiry consumer rollback. The first public attempt also produced a genuine validator disagreement, while a later attempt correctly recorded an ambiguous quote; neither created standing. The successful public fixture is authenticated by immutable commitments from the two configured authority principals. The two hosts are distinct retrieval paths, not a claim of institutional independence. See the transaction-by-transaction record in `docs/DEPLOYMENT_EVIDENCE.md`.

## Non-goals

No legal advice, lawsuit decisions, verdicts on underlying claims, confidential records, payment extraction, social-identity inference, blind trust of one LLM or only one webpage, frontend, API server, token issuance, or simulated StudioNet “proof”.

MIT licence; use at your own risk. Standing is a procedural eligibility primitive, not a merits adjudicator or legal decision-maker.
