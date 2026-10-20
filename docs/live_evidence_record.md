# Live authenticated public-interest evidence record

This is a reproducibility record for the Standing StudioNet lifecycle test. It is
not an institutional attestation and must not be treated as independent from the
repository owner. The underlying transaction is public and independently
inspectable in the official StudioNet explorer.

- Claimant wallet: `0x951e6B75530774fF82321a5ae54e14F778F0C855`
- Frozen matter reference: `x49d04512a08e9eb196e1b382e28cfb79c9f53163ec40cd51b65bc9169ce1358f`
- Underlying StudioNet transaction: `0x49d04512a08e9eb196e1b382e28cfb79c9f53163ec40cd51b65bc9169ce1358f`
- Official explorer record: <https://explorer-studio.genlayer.com/tx/0x49d04512a08e9eb196e1b382e28cfb79c9f53163ec40cd51b65bc9169ce1358f>
- Frozen material-interest criterion: the exact claimant wallet is the sender of
  the exact public StudioNet transaction identified by the frozen matter
  reference, establishing a direct on-chain relationship to the procedural
  matter.

The `x`-prefixed reference is the transaction hash without its leading `0`,
chosen so the repository-local CLI cannot coerce the reference into an integer.
It is an exact contiguous substring of the explorer hash and is intentionally
bound to the full hash above.
