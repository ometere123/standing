# Standing — submission draft

## Status

**BLOCKED — deployment evidence is intentionally absent until redirect safety is verified.**

## Project title

Standing — consensus-backed procedural eligibility for challenge initiation

## Description (under 1,000 characters)

Standing is a reusable GenLayer Intelligent Contract primitive for procedural challenge eligibility. A frozen charter defines the material-interest test and policy; a frozen matter commits its reference, controller, authorities, lifetime and registered actors. Known direct parties receive deterministic standing. An unregistered wallet may petition only for itself, using two configured public sources. A leader and validators independently fetch and assess both sources, and positive quotes must be source-grounded and agree on bounded verdict fields. Approved public eligibility is short-lived and cannot outlive the matter. ProtectedChallenge demonstrates typed consumer gating, caller binding and single-use replay protection. Standing does not decide dispute merits, guilt, damages or legal standing.

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

- 39 offline checks passed.
- 12 stable Direct Mode checks passed with `genlayer-test==0.29.0` and GenVM artifact `v0.2.12`; these use mocked web/LLM observations.
- `genvm-linter==0.11.0` stable checks and schemas passed for both contracts.
- RPC `eth_chainId` independently returned `0xf22f`, parsed as `61999`.

## Deployment proof

None. The deployment script stops before submission because the stable hosted `gl.nondet.web.render` runtime does not expose effective redirect/no-redirect enforcement. An initial hostname check cannot prove redirected evidence stayed on the configured authority, so no value-bearing public-standing deployment is claimed.

## Limitations

Source authority, wallet-to-human identity and independence of two hostnames remain policy assumptions. Public evidence is not cryptographic authorship. Redirect safety is an unresolved launch blocker. Direct Mode is not live StudioNet consensus. See `docs/THREAT_MODEL.md` and `docs/DEPLOYMENT_EVIDENCE.md`.
