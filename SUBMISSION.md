# Standing — submission draft

## Status

**PENDING FINAL DEPLOYMENT EVIDENCE — source-level and stable local security gates pass.**

## Project title

Standing — consensus-backed procedural eligibility for challenge initiation

## Description (under 1,000 characters)

Standing is a reusable GenLayer Intelligent Contract primitive for procedural challenge eligibility. A frozen charter defines the material-interest test and policy; a frozen matter commits its reference, controller, authorities, lifetime and registered actors. Known direct parties receive deterministic standing. An unregistered wallet may petition only for itself after two distinct authority principals immutably commit the exact evidence bytes for that wallet and matter. A leader and validators independently hash-authenticate and semantically assess both public sources, so redirects to changed content fail closed. Approved public eligibility is short-lived and cannot outlive the matter. ProtectedChallenge demonstrates typed consumer gating, caller binding and single-use replay protection. Standing does not decide dispute merits, guilt, damages or legal standing.

## Repository

https://github.com/ometere123/standing

## Required deployment fields

- Network: `studionet`
- Chain ID: `61999`
- RPC: `https://studio.genlayer.com/api`
- Repository-local CLI: `0.39.1`
- Standing contract address: **UNRESOLVED — not deployed**
- Official explorer link: **UNRESOLVED — no transaction**
- ProtectedChallenge address: **UNRESOLVED — Standing not finalized**

## Reusability

Builders can deploy Standing, create sealed charters and matters, register deterministic actors, or integrate the typed `IStanding.is_eligible(matter_id, expected_matter_hash, claimant)` view from another Intelligent Contract. The bundled consumer pins one protected matter and records one-use challenge keys.

## Verified locally

- 43 offline checks passed.
- 16 stable Direct Mode checks passed with `genlayer-test==0.29.0` and GenVM artifact `v0.2.12`; these use mocked web/LLM observations.
- `genvm-linter==0.11.0` stable checks and schemas passed for both contracts.
- RPC `eth_chainId` independently returned `0xf22f`, parsed as `61999`.

## Deployment proof

Pending. Stable `gl.nondet.web.render` does not expose an effective final host, so the submitted implementation authenticates exact rendered bytes with immutable authority commitments. The derived proof gate passes; final addresses, receipts and live lifecycle links must be added only after actual finalized StudioNet transactions.

## Limitations

Authority-principal identity, wallet-to-human identity and institutional independence of two hosts remain policy assumptions. A colluding pair of trusted authorities can precommit misleading content; redirects remain an availability risk even though changed bytes cannot authorize. Direct Mode is not live StudioNet consensus. See `docs/THREAT_MODEL.md` and `docs/DEPLOYMENT_EVIDENCE.md`.
