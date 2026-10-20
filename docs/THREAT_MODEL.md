# Standing security boundaries and abuse cases

## Current release gate

The source and stable local verification are complete, but value-bearing deployment is **BLOCKED**. The exact stable GenVM v0.2.12 source audit shows that `gl.nondet.web.render` validates the requested URL, sends it to the webdriver, and returns only status/body; it does not expose an effective destination or a no-redirect option ([v0.2.12 web module](https://github.com/genlayerlabs/genvm/blob/v0.2.12/modules/install/config/genvm-web-default.lua#L7-L47)). The v0.2.12 webdriver navigates with `page.goto(targetUrl, ...)` and returns page content/status without an effective-host assertion ([v0.2.12 webdriver source](https://github.com/genlayerlabs/genvm/blob/v0.2.12/modules/webdriver/src/prj/src/index.ts#L65-L83)). The v0.2.12 HTTP client is also built with the default `reqwest::ClientBuilder`, so switching to `gl.nondet.web.get` would not establish a no-redirect guarantee ([v0.2.12 client source](https://github.com/genlayerlabs/genvm/blob/v0.2.12/modules/implementation/src/common/mod.rs#L382-L386)). Therefore the contract's initial exact-host check cannot prove that redirected content stayed on the configured host. This is not claimed as solved by consensus: validators can independently agree on the same redirected content.

## Authority and identity

A charter owner alone controls draft charter terms. Once sealed, charter contents/hash are immutable. A matter controller chooses title/reference, scope context, two public source hosts and registered wallets **before activation**. Matter activation hashes all of these including sorted role grants. An active matter cannot be silently edited. Registered addresses are an explicitly trusted issuer assertion. Consumer app must deliberately trust the controller for that matter; Standing never claims independent KYC.

A public claimant cannot claim on behalf of an arbitrary wallet: `file_petition` takes no claimant parameter, uses the transaction sender address and requires that hexadecimal address to appear with the frozen matter reference in two public source excerpts. Merely typing an account holder's name on a webpage is insufficient. Contract-owned wallets may need tailored integration and may not be eligible under public method by default.

## Nondeterminism and validators

Both authority pages are fetched and interpreted inside one GenLayer nondeterministic block. `gl.vm.run_nondet_unsafe` executes a custom validator which re-fetches both URLs and independently runs the same frozen prompt ([Equivalence Principle](https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle)). Verdict class must match **for each source**; positive supporting excerpts must occur verbatim in the independent source and must equal the validator's independently selected quote. Leader fabrication of excerpts, replacement of one authoritative URL with another, malformed responses and material source changes do not count as consensus. The shape validator demands exactly two source outcomes with bounded reason/quote fields.

A source can lie, spoof a wallet in text, be compromised, redirect, disappear or change between leader and validator. Defenses here: frozen domains; literal wallet/matter anchored quotes; two independent-host policy; excerpt grounding; independent validator consensus; short expiry; no public access on disagreement. Residual: operators/redirects and same upstream content are **not proven independent**, nor is the truth of the source. High-stakes consumers must select and validate authoritative source policy externally.

## Lifecycle / permissions

- Unsealed charter cannot back an active matter.
- Matter registration is permitted only during DRAFT and only by matter controller.
- Grant roles are restricted to DIRECT_PARTY and REGISTERED_DEPENDENT. No AI-created third party role.
- Activated matter definition hash and grants are immutable.
- Matter controller can close matter at any time (immediately disables eligibility); not silently reversible.
- Public petition is permissionless but claimant == transaction sender; only exact approved hosts are admissible.
- Maximum six petition attempts per `(matter, wallet)` limit spam, though gas costs and source availability are separate economics.
- Public receipts expire after at most 72 hours; expired matters always deny eligibility.
- Re-petition overwrites the prior public claimant status so multiple stale receipts cannot be spliced together.
- Consumer binds exact matter hash, resolves current standing by typed view, then prevents replay of the chosen 32-byte challenge key.

## Known limitations to close in live QA

1. **Redirects — unresolved launch blocker**: the hosted render path must expose and enforce an effective-host/no-redirect policy, or the public positive evidence path must be redesigned to use a runtime-supported primitive. The stable v0.2.12 source also rules out treating `web.get` as a safe workaround: its client is the default redirect-following `reqwest` client and the response has no effective URL. Until then, no value-bearing deployment is permitted. Same-host, cross-host, attacker-host, internal-host, encoded-URL and user-information bypass cases are covered by the direct URL parser tests where they are locally testable; the hosted redirect result itself cannot be proven from this environment.
2. **Direct Mode mock compatibility**: Direct Mode fixture API may shift with SDK version; the checked-in fixture forces the stable v0.2.12 artifact selector and the suite was run with `genlayer-test==0.29.0`.
3. **GenVM linter/runtime API**: both contracts pass `genvm-linter==0.11.0` `check` and schema extraction against `GENVM_VERSION=v0.2.12`; this is stable local compatibility evidence, not a finalized StudioNet deployment receipt.
4. **Remote attestation quality**: page text and exact quote give provenance within a fetched page, not cryptographic authorship or publication-date proof. Use long-lived public authoritative records, not short-lived chat pages.
5. **Time**: live test boundary at `valid_until` and `expires_at`; a read is valid only at current chain time. No off-chain cached grant should be relied on after expiry.
6. **Jurisdiction**: this is a technical protocol eligibility gate, not a legal doctrine or regulator decision.
7. **Registration capture**: a dishonest matter controller may register its own participants or close matters. Consumers must trust the controller's configuration or use stronger external governance.
8. **Two-host independence**: sibling-host guard is a heuristic, not a public-suffix or ultimate ownership attestation.

## Adversarial review matrix

| Attack | Expected invariant |
|---|---|
| Different caller uses victim evidence | Fails wallet-anchor check; cannot specify victim as caller |
| Claimed wallet only appears in page script | Do not count unless independently readable text and substantively material |
| Forged quote from leader | Validator must find literal quote in independent page; reject |
| One source unavailable | `UNAVAILABLE`; no eligibility |
| Both domains same operator | Source policy trust risk; not claim third-party independence |
| URL userinfo, encoded path, query/fragment, port, non-HTTPS | Pre-consensus rejection |
| Leader says SUPPORTED without quote | Shape rejection |
| Validator disagrees on one page | No consensus finality; no standing |
| Repeated rejected petition | Attempts increment; after six reject |
| Valid petition then new invalid petition | Latest claimant verdict determines access |
| Reuse evidence for different matter | Requires exact frozen reference on both pages |
| Controller adds party after activation | Rejected; hash immutable |
| Caller swaps expected matter hash | `is_eligible` false |
| Use after matter closes/expires | `is_eligible` false |
| Same challenge key again | Rejected by consumer |

## Verification recorded for this revision

- Offline suite: 39 passed.
- Stable Direct Mode: 12 passed with `genlayer-test==0.29.0` and the v0.2.12 artifact selector. Web/LLM responses are mocks and are not live consensus evidence.
- Stable GenVM checks: `genvm-linter==0.11.0`, `GENVM_VERSION=v0.2.12`, both contracts pass lint/validation and schema extraction.
- Network guard: repository-local CLI `0.39.1`; `eth_chainId` at `https://studio.genlayer.com/api` returned `0xf22f`, independently parsed as `61999`.
- Deployment: intentionally not performed because the redirect blocker above is unresolved. No address, transaction, finalized execution or live lifecycle claim is valid for this revision.
