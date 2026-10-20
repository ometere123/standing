# Standing security boundaries and abuse cases

## Current release gate

The exact stable GenVM v0.2.12 source audit confirms that `gl.nondet.web.render` follows navigation without exposing an effective destination or a no-redirect option ([v0.2.12 web module](https://github.com/genlayerlabs/genvm/blob/v0.2.12/modules/install/config/genvm-web-default.lua#L7-L47), [v0.2.12 webdriver source](https://github.com/genlayerlabs/genvm/blob/v0.2.12/modules/webdriver/src/prj/src/index.ts#L65-L83)). The v0.2.12 HTTP client also uses default redirect behavior, so switching to `gl.nondet.web.get` would not establish a no-redirect guarantee ([v0.2.12 client source](https://github.com/genlayerlabs/genvm/blob/v0.2.12/modules/implementation/src/common/mod.rs#L382-L386)).

Standing does not treat the initial hostname as evidence authenticity. Instead, two configured authority principals authenticate exact rendered bytes by submitting immutable Keccak-256 commitments after matter activation. The petition path will not invoke semantic consensus unless both commitments match the exact `(matter, frozen matter hash, claimant, source)` tuple. The leader and validator each fetch both URLs, recompute both hashes, and only then assess the frozen criterion. Redirected content that differs from the precommitted bytes fails closed; a redirect that serves identical committed bytes does not create a new authorization and remains subject to the same semantic consensus. The residual redirect risk is availability and distribution ambiguity, not content substitution.

## Authority and identity

A charter owner alone controls draft charter terms. Once sealed, charter contents/hash are immutable. A matter controller chooses title/reference, scope context, two public source hosts, two distinct nonzero authority principals and registered wallets **before activation**. Matter activation hashes all of these including sorted role grants. An active matter cannot be silently edited. Registered addresses are an explicitly trusted issuer assertion. Consumer app must deliberately trust the controller for that matter; Standing never claims independent KYC.

An authority principal can commit one canonical lowercase 32-byte content hash for one source and claimant exactly once per matter. The caller must equal the authority frozen for that source; a controller, claimant or other wallet cannot write the commitment. Commitments cannot be changed after activation, closure or expiry. The commitment authenticates bytes and the on-chain tuple, not the real-world truth of the document, the identity behind the wallet or the institutional independence of the authority.

A public claimant cannot claim on behalf of an arbitrary wallet: `file_petition` takes no claimant parameter, uses the transaction sender address and requires that hexadecimal address to appear with the frozen matter reference in two authority-committed public source excerpts. Merely typing an account holder's name on a webpage is insufficient. Contract-owned wallets may need tailored integration and may not be eligible under public method by default.

## Nondeterminism and validators

Both authority pages are fetched and interpreted inside one GenLayer nondeterministic block. `gl.vm.run_nondet_unsafe` executes a custom validator which re-fetches both URLs, independently recomputes both commitments and independently runs the same frozen prompt ([Equivalence Principle](https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle)). Verdict class must match **for each source**; positive supporting excerpts must occur verbatim in the independently retrieved committed source and must equal the validator's independently selected quote. Leader fabrication of excerpts, replacement of one authority's content, malformed responses, redirect substitution and material source changes do not count as consensus. The shape validator demands exactly two source outcomes with bounded reason/quote fields.

A source can lie, spoof a wallet in text, be compromised, redirect, disappear or change between leader and validator. Defenses here: frozen domains; sender-authenticated immutable authority commitments; literal wallet/matter anchored quotes; two independent-principal/host policy; excerpt grounding; independent validator consensus; short expiry; no public access on disagreement. Residual: the authority principals can be dishonest or collude, a redirect can cause denial of service, and two hosts/principals are **not proven institutionally independent**. High-stakes consumers must select and validate authority policy externally.

## Lifecycle / permissions

- Unsealed charter cannot back an active matter.
- Matter registration is permitted only during DRAFT and only by matter controller.
- Grant roles are restricted to DIRECT_PARTY and REGISTERED_DEPENDENT. No AI-created third party role.
- Activated matter definition hash and grants are immutable.
- Matter controller can close matter at any time (immediately disables eligibility); not silently reversible.
- Public petition is permissionless but claimant == transaction sender; only exact approved hosts and two valid immutable authority commitments are admissible.
- Evidence commitments are one-time and matter-bound; missing, stale, substituted or mismatched commitments produce denial without running the model.
- Maximum six petition attempts per `(matter, wallet)` limit spam, though gas costs and source availability are separate economics.
- Public receipts expire after at most 72 hours; expired matters always deny eligibility.
- Re-petition overwrites the prior public claimant status so multiple stale receipts cannot be spliced together.
- Consumer binds exact matter hash, resolves current standing by typed view, then prevents replay of the chosen 32-byte challenge key.

## Known limitations

1. **Redirects remain an availability risk**: stable v0.2.12 does not expose an effective final host, but changed redirected bytes fail the immutable content-hash check before semantic assessment. A redirect serving the exact committed bytes is safe against content substitution, not proof of current authority control. A redirect can still cause unavailable evidence and denial.
2. **Authority trust**: the two principals are explicitly configured and transaction-authenticated, but the contract cannot prove their institutional identity, key custody, or independence. A colluding pair can precommit misleading documents; this is a declared trust assumption, not an LLM failure.
3. **Direct Mode mock compatibility**: Direct Mode fixture API may shift with SDK version; the checked-in fixture forces the stable v0.2.12 artifact selector and the suite was run with `genlayer-test==0.29.0`.
4. **GenVM linter/runtime API**: both contracts pass `genvm-linter==0.11.0` `check` and schema extraction against `GENVM_VERSION=v0.2.12`; this is stable local compatibility evidence, not a finalized StudioNet deployment receipt.
5. **Remote evidence quality**: page text and exact quote prove only that the committed bytes contained the asserted material; they do not prove real-world truth, publication date or wallet-to-human identity. Use long-lived authoritative records.
6. **Time**: live test boundary at `valid_until` and `expires_at`; a read is valid only at current chain time. No off-chain cached grant should be relied on after expiry.
7. **Jurisdiction**: this is a technical protocol eligibility gate, not a legal doctrine or regulator decision.
8. **Registration capture**: a dishonest matter controller may register its own participants or close matters. Consumers must trust the controller's configuration or use stronger external governance.
9. **Two-host independence**: sibling-host guard is a heuristic, not a public-suffix or ultimate ownership attestation.

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
| Redirect substitutes changed page bytes | Immutable hash mismatch produces `NOT_SUPPORTED`; no model assessment or grant |
| Untrusted wallet submits a commitment | Sender must equal the frozen source authority; write rejected |
| Authority tries to rewrite a commitment | One-time commitment is immutable; write rejected |
| Commitment from another matter/wallet/source | Tuple fields and storage key must match; petition denied |
| Reuse evidence for different matter | Requires exact frozen reference on both pages |
| Controller adds party after activation | Rejected; hash immutable |
| Caller swaps expected matter hash | `is_eligible` false |
| Use after matter closes/expires | `is_eligible` false |
| Same challenge key again | Rejected by consumer |

## Verification recorded for this revision

- Offline suite: 43 passed.
- Stable Direct Mode: 16 passed with `genlayer-test==0.29.0` and the v0.2.12 artifact selector. Web/LLM responses are mocks and are not live consensus evidence.
- Stable GenVM checks: `genvm-linter==0.11.0`, `GENVM_VERSION=v0.2.12`, both contracts pass lint/validation and schema extraction.
- Network guard: repository-local CLI `0.39.1`; `eth_chainId` at `https://studio.genlayer.com/api` returned `0xf22f`, independently parsed as `61999`.
- Deployment: Standing and all three consumer instances are finalized on stable StudioNet and their deployed sources are matched to the recorded hashes. Matter 5 provides a live one-hour expiry proof: after `expires_at`, canonical eligibility returned false and the post-expiry consumer rollback created no challenge record.
