# Standing — submission handoff

## Status

**READY FOR SUBMISSION.** Source, security, stable-runtime, deployment, live lifecycle and CI evidence are complete. The documented authority and redirect limitations remain explicit trust/availability assumptions, not unresolved deployment blockers.

## Project title

Standing — consensus-backed procedural eligibility for challenge initiation

## Description (under 1,000 characters)

Standing is a reusable GenLayer Intelligent Contract primitive for procedural challenge eligibility. A sealed charter freezes the material-interest test and petition policy; an activated matter freezes its reference, authorities, lifetime and registered actors. Known direct parties receive deterministic standing. An unregistered wallet may petition only for itself after two distinct authority principals immutably commit the exact evidence bytes for that wallet and matter. The leader and validators independently hash-authenticate and semantically assess both public sources, so changed redirected content fails closed. Approved public eligibility is short-lived and cannot outlive the matter. ProtectedChallenge demonstrates typed consumer gating, caller binding and single-use replay protection. Standing does not decide dispute merits, guilt, damages or legal standing.

## Repository

https://github.com/ometere123/standing

## Verified deployment

- Network: `studionet`
- Chain ID: `61999`
- RPC: `https://studio.genlayer.com/api`
- Repository-local CLI: `genlayer@0.39.1`
- Standing: [`0x5b27dB099296AAF72f7F36f458cbdD79B9f64d4f`](https://explorer-studio.genlayer.com/address/0x5b27dB099296AAF72f7F36f458cbdD79B9f64d4f)
- Standing deployment: [`0x3ea2eab1c2f77421a75fad7ce16cc2ac96e29fe9e55096e672a6bb31dc439ce8`](https://explorer-studio.genlayer.com/tx/0x3ea2eab1c2f77421a75fad7ce16cc2ac96e672a6bb31dc439ce8)
- ProtectedChallenge (direct): [`0xb894c8769f38Ee4685Edc26710edB3D0c12F7bB0`](https://explorer-studio.genlayer.com/address/0xb894c8769f38Ee4685Edc26710edB3D0c12F7bB0)
- ProtectedChallenge (public): [`0x28AbC74d187F8c8dA258e8d4f6267cFE4DFb60b2`](https://explorer-studio.genlayer.com/address/0x28AbC74d187F8c8dA258e8d4f6267cFE4DFb60b2)
- ProtectedChallenge (expiry): [`0xBea9ac6AB160418FA59d602A944df01d938EB05E`](https://explorer-studio.genlayer.com/address/0xBea9ac6AB160418FA59d602A944df01d938EB05E)
- All deployments finalized with execution success and pin the actual Standing address.

## Reusability

Builders can deploy Standing, seal their own charter, activate matters with frozen hashes, register direct/dependent actors, or integrate the typed `IStanding.is_eligible(matter_id, expected_matter_hash, claimant)` view from another Intelligent Contract. Consumers must pin their intended matter and pass the actual caller address.

## Verified engineering evidence

- Offline: **43 passed**.
- Stable Direct Mode: **16 passed** with `genlayer-test==0.29.0`, stable GenVM `v0.2.12`; web/LLM observations are mocks.
- `genvm-linter==0.11.0`: both deployable contracts validated and schemas extracted successfully.
- `eth_chainId` independently returned `0xf22f` (`61999`).
- Live: registered-party challenge success; wrong-wallet, replay and closed-matter rollbacks; authenticated two-source public grant; typed public consumer success; missing-commitment denial; validator disagreement and ambiguous-quote fail-closed records; a real one-hour expiry followed by `is_eligible=false` and a post-expiry consumer rollback with no challenge mutation.

## Security and limitations

Stable v0.2.12 does not expose an enforceable final redirect-host check, and its HTTP path also follows redirects. Standing therefore authenticates exact rendered bytes with immutable sender-authenticated authority commitments before semantic assessment. This blocks changed redirected content from manufacturing a grant, but redirects remain an availability risk. Authority identity, key custody, institutional independence and real-world truth remain configured trust assumptions. The live one-hour expiry boundary is proven in `docs/DEPLOYMENT_EVIDENCE.md`; Direct Mode additionally covers the broader expiry matrix.

## Source hashes

- `contracts/standing.py`: `A72F202727FCE84816160D12A2D8557A959933CB3DC3AB2F7DF8B51368D3F3EC`
- `contracts/protected_challenge.py`: `780AFC3D8F4740E25BA8CB521395319EC37C25234789D80E3D2F23533570AF97`

See `docs/DEPLOYMENT_EVIDENCE.md` for the complete receipt and lifecycle index.
