# Standing StudioNet deployment evidence

## Final status

**FINALIZED on stable StudioNet.** This record separates deterministic state transitions, live GenLayer consensus results, and mock-based Direct Mode tests. No preview network, chain 61997, or global CLI was used.

Observed on `2026-10-20`:

- Network: `studionet`
- Chain ID: `61999`
- RPC: `https://studio.genlayer.com/api`
- Repository-local CLI: `genlayer@0.39.1`
- Independent RPC proof: `eth_chainId = 0xf22f`, parsed as decimal `61999`
- Stable GenVM artifact: `v0.2.12`
- Linter: `genvm-linter==0.11.0`
- Direct Mode SDK: `genlayer-test==0.29.0`
- Authenticated-evidence gate: `AUTHENTICATED_EVIDENCE_STATUS=VERIFIED`

The stable v0.2.12 web renderer follows redirects without exposing an enforceable effective-host result. Standing therefore does not treat the submitted URL hostname as content authenticity. Two configured authority principals immutably commit the exact rendered bytes for each `(matter, frozen matter hash, claimant, source)` tuple. Both leader and validator fetch, hash-check and semantically assess both sources; a changed redirect fails closed before a grant can be produced. This protects against content substitution, while redirect availability and authority independence remain explicit limitations.

## Local verification

- Python compilation: passed for `contracts`, `tests` and `scripts`
- Offline suite: **43 passed**
- Stable Direct Mode suite: **16 passed**; web and LLM observations are mocks, not live consensus evidence
- Stable GenVM validation: both deployable contracts passed under `GENVM_VERSION=v0.2.12`
- Schema extraction: passed for both deployable contracts
- Static preflight: passed
- Authenticated-evidence security gate: passed
- `npm ci`: passed
- Repository-local CLI version: exactly `0.39.1`
- GitHub Actions: [run 39442796728](https://github.com/ometere123/standing/actions/runs/39442796728) passed both `offline` and `direct` jobs for commit `d3e423eae0f498b602d929de70f95326cc9f5b26`

## Source identity

The deployed Standing source was retrieved from chain and matched byte-for-byte after normalizing the CLI's omitted final newline.

- `contracts/standing.py`: `A72F202727FCE84816160D12A2D8557A959933CB3DC3AB2F7DF8B51368D3F3EC`
- `contracts/protected_challenge.py`: `780AFC3D8F4740E25BA8CB521395319EC37C25234789D80E3D2F23533570AF97`

The final committed manifest is `SOURCE_SHA256_MANIFEST.json`.

## Standing deployment

- Address: [`0x5b27dB099296AAF72f7F36f458cbdD79B9f64d4f`](https://explorer-studio.genlayer.com/address/0x5b27dB099296AAF72f7F36f458cbdD79B9f64d4f)
- Deployment transaction: [`0x3ea2eab1c2f77421a75fad7ce16cc2ac96e29fe9e55096e672a6bb31dc439ce8`](https://explorer-studio.genlayer.com/tx/0x3ea2eab1c2f77421a75fad7ce16cc2ac96e29fe9e55096e672a6bb31dc439ce8)
- Final status: `FINALIZED`; execution result `SUCCESS`
- Source match: verified against the final `contracts/standing.py` hash above

## ProtectedChallenge deployments

### Direct-party proof consumer

- Address: [`0xb894c8769f38Ee4685Edc26710edB3D0c12F7bB0`](https://explorer-studio.genlayer.com/address/0xb894c8769f38Ee4685Edc26710edB3D0c12F7bB0)
- Deployment transaction: [`0x87de40283044927e05fc2c677bd48edb2e7138408cb224ddae0d85b50909edde`](https://explorer-studio.genlayer.com/tx/0x87de40283044927e05fc2c677bd48edb2e7138408cb224ddae0d85b50909edde)
- Final status: `FINALIZED`; execution result `SUCCESS`
- Constructor binding: Standing `0x5b27dB099296AAF72f7F36f458cbdD79B9f64d4f`, matter `1`, hash `7a3aa5279a4f1ffd6175c6702629a9e13f42f235a4126b36944c9fe3e4078312`

### Authenticated public-interest proof consumer

- Address: [`0x28AbC74d187F8c8dA258e8d4f6267cFE4DFb60b2`](https://explorer-studio.genlayer.com/address/0x28AbC74d187F8c8dA258e8d4f6267cFE4DFb60b2)
- Deployment transaction: [`0x423cb183b398e157c4ca083bd9ade23b22774fd78c3c40516a53bc9668039b48`](https://explorer-studio.genlayer.com/tx/0x423cb183b398e157c4ca083bd9ade23b22774fd78c3c40516a53bc9668039b48)
- Final status: `FINALIZED`; execution result `SUCCESS`
- Constructor binding: Standing `0x5b27dB099296AAF72f7F36f458cbdD79B9f64d4f`, matter `3`, hash `0d344ee8056eb97b4524172e6323a147d91cfcb6d9cfc806dd1a48c5f6d635de`

### Live-expiry proof consumer

- Address: [`0xBea9ac6AB160418FA59d602A944df01d938EB05E`](https://explorer-studio.genlayer.com/address/0xBea9ac6AB160418FA59d602A944df01d938EB05E)
- Deployment transaction: [`0xb990f5caf4e01498e62b00dda95e4ff81072249002b1e97bc90c1e5629394235`](https://explorer-studio.genlayer.com/tx/0xb990f5caf4e01498e62b00dda95e4ff81072249002b1e97bc90c1e5629394235)
- Final status: `FINALIZED`; execution result `SUCCESS`
- Constructor binding: Standing `0x5b27dB099296AAF72f7F36f458cbdD79B9f64d4f`, matter `5`, hash `f3da592ae57bd5ebec34ce3821fb4b94a83e40728b4d4d42bf20500c5c754155`

## Live lifecycle records

All links below are stable StudioNet explorer transaction links. Failed cases are finalized rollbacks and did not create successful challenge records.

### Deterministic registered-party standing

- Charter creation: [`0x105a3bf82c75abe5df3cb8ebaa03ca69aaf0538ee6f0024efffd5d5b074203a2`](https://explorer-studio.genlayer.com/tx/0x105a3bf82c75abe5df3cb8ebaa03ca69aaf0538ee6f0024efffd5d5b074203a2)
- Charter seal: [`0x7ba5ac4d7bf3b8353a0d0913a72230081fb17b5155604b1f7f0fb9d596a4116c`](https://explorer-studio.genlayer.com/tx/0x7ba5ac4d7bf3b8353a0d0913a72230081fb17b5155604b1f7f0fb9d596a4116c)
- Matter creation: [`0x4be312444e9b1d8a9804fceb2c06c42ac4924b4de92ff8a1e216aa1c5140d26e`](https://explorer-studio.genlayer.com/tx/0x4be312444e9b1d8a9804fceb2c06c42ac4924b4de92ff8a1e216aa1c5140d26e)
- Direct-party registration: [`0xe90e15ae253721621af14518a1b0a4029eaba5194d39e1cdd843e649dd2fcecf`](https://explorer-studio.genlayer.com/tx/0xe90e15ae253721621af14518a1b0a4029eaba5194d39e1cdd843e649dd2fcecf)
- Matter activation: [`0xfc64b658cea91db6798b18e114c883bbf91b968f8a1fa1f58649c0da64f0966c`](https://explorer-studio.genlayer.com/tx/0xfc64b658cea91db6798b18e114c883bbf91b968f8a1fa1f58649c0da64f0966c)
- Frozen matter hash: `7a3aa5279a4f1ffd6175c6702629a9e13f42f235a4126b36944c9fe3e4078312`
- Successful typed consumer challenge: [`0x948b3c8bca077574d844933a298f48ca4a4af6ff33d8f1a66e1a2b2fe74f5c37`](https://explorer-studio.genlayer.com/tx/0x948b3c8bca077574d844933a298f48ca4a4af6ff33d8f1a66e1a2b2fe74f5c37)

### Unauthorized and replay protection

- Wrong wallet rollback (`claimant lacks current standing`): [`0xa572d9911fa0ad2c73ee759b02b6d39c3829f4728946a070ad81e0a9a22c9b49`](https://explorer-studio.genlayer.com/tx/0xa572d9911fa0ad2c73ee759b02b6d39c3829f4728946a070ad81e0a9a22c9b49)
- Replay rollback (`challenge already submitted`): [`0xc3b58439506dc846ac95dbe92e43ee2dd7fc0f8c853748e78573c69c26cebf26`](https://explorer-studio.genlayer.com/tx/0xc3b58439506dc846ac95dbe92e43ee2dd7fc0f8c853748e78573c69c26cebf26)
- Matter closure: [`0xcdae36dda2297c723b133718a4ff143a1b7f9e2f166d2722ff0027d8c5272013`](https://explorer-studio.genlayer.com/tx/0xcdae36dda2297c723b133718a4ff143a1b7f9e2f166d2722ff0027d8c5272013)
- Closed-matter rollback: [`0xcb4a74f9a8b6a477415ce488cda8583f1ce0d912d57500614f29495c07f08f04`](https://explorer-studio.genlayer.com/tx/0xcb4a74f9a8b6a477415ce488cda8583f1ce0d912d57500614f29495c07f08f04)

### Authenticated public-interest standing

The compact fixture was published in commit `76cef31dd824f712c54477ed9f8db1bbca543c83`. Stable v0.2.12 rendered both URLs to 1,066 bytes with the same Keccak-256 hash `50c4fe2ffb40735a3d33a701f3e6d36dc7ae57be0e15a049421d0743c620bc18`. The fixture is a repository-published reproducibility record, not institutional proof; the two authority principals authenticate exact bytes, not real-world identity or source independence.

- Raw fixture: [GitHub raw](https://raw.githubusercontent.com/ometere123/standing/76cef31dd824f712c54477ed9f8db1bbca543c83/docs/live_evidence_record_compact.md)
- Alternate fixture path: [Statically](https://cdn.statically.io/gh/ometere123/standing/76cef31dd824f712c54477ed9f8db1bbca543c83/docs/live_evidence_record_compact.md)
- Public charter creation: [`0xfc9d0e5a577c2affe4c91811d03f7672f3535918940377ef83da6504b501ed86`](https://explorer-studio.genlayer.com/tx/0xfc9d0e5a577c2affe4c91811d03f7672f3535918940377ef83da6504b501ed86)
- Public charter seal: [`0x291f89c037fbe20e4b589ff11e7999963e396a3bd8db57400c9fc1c6c919a9cd`](https://explorer-studio.genlayer.com/tx/0x291f89c037fbe20e4b589ff11e7999963e396a3bd8db57400c9fc1c6c919a9cd)
- Matter 3 creation: [`0x6f7a5ca1f82f8850a1ecd1614130374cf1829f9cad540fdb596d00f28e1959b3`](https://explorer-studio.genlayer.com/tx/0x6f7a5ca1f82f8850a1ecd1614130374cf1829f9cad540fdb596d00f28e1959b3)
- Matter 3 activation: [`0x2e66725e98b74d71a5b6b716d6118743dc9b86ed11ac19060510e53dcde7b427`](https://explorer-studio.genlayer.com/tx/0x2e66725e98b74d71a5b6b716d6118743dc9b86ed11ac19060510e53dcde7b427)
- Matter 3 frozen hash: `0d344ee8056eb97b4524172e6323a147d91cfcb6d9cfc806dd1a48c5f6d635de`
- Authority A commitment: [`0x1b16344a7037fe47bcfed377cef3bd3816ca17bb461acdc1ed3508efd1c3ed31`](https://explorer-studio.genlayer.com/tx/0x1b16344a7037fe47bcfed377cef3bd3816ca17bb461acdc1ed3508efd1c3ed31)
- Authority B commitment: [`0xd573a9358ffc829f9942996026d39675640657ff74d39e363db032f23a521e9f`](https://explorer-studio.genlayer.com/tx/0xd573a9358ffc829f9942996026d39675640657ff74d39e363db032f23a521e9f)
- Successful two-source petition (petition 2, result `P_GRANTED`): [`0xcd6ab1e8c0b7f15bcdf8beb9c1921bcf1af3a6352e95d4c76bd9c81dc7834417`](https://explorer-studio.genlayer.com/tx/0xcd6ab1e8c0b7f15bcdf8beb9c1921bcf1af3a6352e95d4c76bd9c81dc7834417)
- Canonical readback: petition 2 had two `SUPPORTED` verdicts, the same committed hash on both sources, and a nonzero `valid_until`; `is_eligible(3, frozen_hash, walletA)` returned `true`.
- Successful public claimant consumer challenge: [`0x721bdc08ad8fd788da6d7f6ae9f11247927808ab1d50cb68e17b3ee9fbc1d781`](https://explorer-studio.genlayer.com/tx/0x721bdc08ad8fd788da6d7f6ae9f11247927808ab1d50cb68e17b3ee9fbc1d781)
- Canonical consumer readback: challenge key `d555…` stored opener walletA, matter 3 and the exact frozen hash.

### Live expiry and post-expiry consumer rollback

- Matter 5 creation: [`0x06f74234a3461632ad8962bac9e4d74befa644d5a17dc688d75eaa037b79c9ab`](https://explorer-studio.genlayer.com/tx/0x06f74234a3461632ad8962bac9e4d74befa644d5a17dc688d75eaa037b79c9ab)
- Matter 5 activation: [`0x38a3c1ee340f7aa4ab6531b315a630a0ec210d77c12cb08bb85897efe2f79c74`](https://explorer-studio.genlayer.com/tx/0x38a3c1ee340f7aa4ab6531b315a630a0ec210d77c12cb08bb85897efe2f79c74)
- Matter 5 reference: `x49d04512a08e9eb196e1b382e28cfb79c9f53163ec40cd51b65bc9169ce1358f`
- Matter 5 frozen hash: `f3da592ae57bd5ebec34ce3821fb4b94a83e40728b4d4d42bf20500c5c754155`
- Recorded `opened_at`: `1792498672`; recorded `expires_at`: `1792502272`
- Authority A commitment: [`0x23a367a56db11050af486615136bc0b6573f7f29096fe078a229da44fb26f7e9`](https://explorer-studio.genlayer.com/tx/0x23a367a56db11050af486615136bc0b6573f7f29096fe078a229da44fb26f7e9)
- Authority B commitment: [`0x3df7c16dbc082e2aab407852b677fd30a23da2e623b8e41801691bb340af2f58`](https://explorer-studio.genlayer.com/tx/0x3df7c16dbc082e2aab407852b677fd30a23da2e623b8e41801691bb340af2f58)
- Successful authenticated petition: [`0xca043a768bbfcf45c7aed3ed343fff3dcf5ac7ee3bb8389128eae2f5873c59cd`](https://explorer-studio.genlayer.com/tx/0xca043a768bbfcf45c7aed3ed343fff3dcf5ac7ee3bb8389128eae2f5873c59cd); finalized `MAJORITY_AGREE`, petition result `P_GRANTED`, both source verdicts `SUPPORTED`, `valid_until=1792502272`.
- Post-expiry canonical readback: after the latest StudioNet block timestamp reached `1792507227`, `get_matter(5)` and `get_petition(5)` still showed the frozen hash and grant receipt, while `is_eligible(5, f3da..., walletA)` returned `false` because the recorded expiry had passed.
- Post-expiry consumer rollback: [`0x7c9a6a5ce9a68024648d09e615aeadb693063cd576ec430e899d1af57c55f2fd`](https://explorer-studio.genlayer.com/tx/0x7c9a6a5ce9a68024648d09e615aeadb693063cd576ec430e899d1af57c55f2fd) finalized `MAJORITY_AGREE` on `EXPECTED: claimant lacks current standing`; the fresh challenge key was not stored.

### Negative public evidence and consensus disagreement

- First public attempt against matter 2: [`0x3180582db5b642e55ace96c9db7d0f65b7c9830d86054c8c644ef7eaf4e682cb`](https://explorer-studio.genlayer.com/tx/0x3180582db5b642e55ace96c9db7d0f65b7c9830d86054c8c644ef7eaf4e682cb) finalized `MAJORITY_DISAGREE`; no petition state was created.
- Retry against matter 2: [`0x1e348fed0a3e6235186fa62ed1b5ed42d982d2e718e5b4427e8aa334ff133a83`](https://explorer-studio.genlayer.com/tx/0x1e348fed0a3e6235186fa62ed1b5ed42d982d2e718e5b4427e8aa334ff133a83) finalized `MAJORITY_AGREE` but recorded `P_AMBIGUOUS` because the returned quote failed literal source binding; it did not grant standing.
- Unregistered wallet with no authority commitments: [`0x8b91365678aa8a97fca58b0673a8549bd0950411f21138e9f15616a60b32be41`](https://explorer-studio.genlayer.com/tx/0x8b91365678aa8a97fca58b0673a8549bd0950411f21138e9f15616a60b32be41) finalized petition 3 as `P_DENIED` with both verdicts `SOURCE_NOT_SUPPORTED` and reason `authenticated source commitment missing or invalid`.

## Remaining limitations

- The live one-hour expiry boundary is now proven: matter 5 expired at `1792502272`, the later StudioNet block timestamp was `1792507227`, `is_eligible` returned `false`, and the consumer rollback created no challenge record.
- The authority principals and their key custody are configured trust assumptions; two addresses and two hostnames do not prove institutional independence.
- A redirect to changed content can cause denial of service; it cannot create a positive grant without matching the immutable commitment.
- Direct Mode web/LLM cases are mocks and must not be represented as live validator evidence.
