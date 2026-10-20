# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
"""A minimal actual consumer of Standing's typed cross-IC view interface."""
from genlayer import *
from dataclasses import dataclass
import typing

@gl.contract_interface
class IStanding:
    class View:
        def is_eligible(self, matter_id: u256, expected_matter_hash: str, claimant: Address) -> bool: ...
    class Write:
        pass

@allow_storage
@dataclass
class Challenge:
    opener: Address
    matter_id: u256
    matter_hash: str
    challenge_key: str

class ProtectedChallenge(gl.Contract):
    standing_address: Address
    protected_matter_id: u256
    protected_matter_hash: str
    challenges: TreeMap[str, Challenge]
    challenge_count: u256

    def __init__(self, standing_address: Address, protected_matter_id: u256, protected_matter_hash: str):
        if str(standing_address).lower() == "0x" + "0" * 40:
            raise gl.vm.UserError('EXPECTED: standing address cannot be zero')
        if int(protected_matter_id) <= 0:
            raise gl.vm.UserError('EXPECTED: protected matter id must be positive')
        if (not isinstance(protected_matter_hash, str) or len(protected_matter_hash) != 64 or
                any(x not in '0123456789abcdef' for x in protected_matter_hash)):
            raise gl.vm.UserError('EXPECTED: invalid protected matter hash')
        self.standing_address = standing_address
        self.protected_matter_id = int(protected_matter_id)
        self.protected_matter_hash = protected_matter_hash
        self.challenge_count = 0

    @gl.public.write
    def open_challenge(self, matter_id: u256, expected_matter_hash: str, challenge_key: str) -> None:
        if len(expected_matter_hash) != 64 or any(x not in '0123456789abcdef' for x in expected_matter_hash):
            raise gl.vm.UserError('EXPECTED: invalid matter hash')
        if len(challenge_key) != 64 or any(x not in '0123456789abcdef' for x in challenge_key):
            raise gl.vm.UserError('EXPECTED: invalid challenge key')
        if (int(matter_id) != int(self.protected_matter_id) or
                expected_matter_hash != str(self.protected_matter_hash)):
            raise gl.vm.UserError('EXPECTED: challenge must target the protected matter')
        if challenge_key in self.challenges:
            raise gl.vm.UserError('EXPECTED: challenge already submitted')
        remote = IStanding(self.standing_address)
        if not remote.view().is_eligible(matter_id, expected_matter_hash, gl.message.sender_address):
            raise gl.vm.UserError('EXPECTED: claimant lacks current standing')
        self.challenges[challenge_key] = Challenge(gl.message.sender_address, matter_id,
                                                   expected_matter_hash, challenge_key)
        self.challenge_count = int(self.challenge_count) + 1

    @gl.public.view
    def get_protected_matter(self) -> dict:
        return {'standing_address': str(self.standing_address),
                'matter_id': int(self.protected_matter_id),
                'matter_hash': str(self.protected_matter_hash)}

    @gl.public.view
    def get_challenge(self, challenge_key: str) -> dict:
        if challenge_key not in self.challenges:
            raise gl.vm.UserError('EXPECTED: unknown challenge')
        c = self.challenges[challenge_key]
        return {'opener': str(c.opener), 'matter_id': int(c.matter_id),
                'matter_hash': str(c.matter_hash), 'challenge_key': str(c.challenge_key)}
