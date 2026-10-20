"""Stable Direct Mode scenarios for pinned genlayer-test 0.29.0.

These are mocked external observations inside the real Direct Mode runner. They
prove contract execution and validator wiring, not live StudioNet consensus.
"""
import json

CONTRACT = 'contracts/standing.py'
CONSUMER = 'contracts/protected_challenge.py'
BASE = '2026-10-19T09:00:00+00:00'
EXPIRED = '2026-10-25T09:00:00+00:00'


def actor(label):
    # Addresses must be created after GenLayer SDK loads, not at import time.
    from gltest.direct import create_address
    return create_address(label)


def create_active(vm, deploy, mode=True, lifetime=3600, extra_actors=(), charter_lifetime=86400):
    vm.warp(BASE)
    c = deploy(CONTRACT)
    cid = c.create_charter('Service failure', 'Material, direct, documented service impact', charter_lifetime, mode)
    charter_hash = c.seal_charter(cid)
    mid = c.create_matter(cid, 'MAT-100', 'Public service failure',
        'A confirmed paid subscriber affected by the public MAT-100 service incident',
        'service.example.com', 'regulator.example.org')
    c.register_actor(mid, actor('alice'), 3)
    for label, role in extra_actors:
        c.register_actor(mid, actor(label), role)
    matter_hash = c.activate_matter(mid, lifetime)
    return c, cid, mid, charter_hash, matter_hash


def mock_supported(vm, wallet):
    vm.clear_mocks()
    page = f'MAT-100 {wallet} is a paid subscriber who suffered a material service loss.'
    vm.mock_web(r'.*service\.example\.com/m.*', {'status': 200, 'body': page})
    vm.mock_web(r'.*regulator\.example\.org/m.*', {'status': 200, 'body': page})
    vm.mock_llm(r'STANDING / PUBLIC MATERIAL-INTEREST ATTESTATION',
        json.dumps({'verdict':'SUPPORTED','quote':page,'reason':'explicit public material interest'}))
    return page


def mock_evidence(vm, page_a, page_b, response):
    vm.clear_mocks()
    vm.mock_web(r'.*service\.example\.com/m.*', {'status': 200, 'body': page_a})
    vm.mock_web(r'.*regulator\.example\.org/m.*', {'status': 200, 'body': page_b})
    vm.mock_llm(r'STANDING / PUBLIC MATERIAL-INTEREST ATTESTATION', response)


def test_registered_party_eligibility_without_llm(direct_vm, direct_deploy):
    c, _, mid, _, h = create_active(direct_vm, direct_deploy)
    alice = actor('alice')
    bob = actor('bob')
    assert c.is_eligible(mid, h, alice)
    assert not c.is_eligible(mid, h, bob)
    assert not c.is_eligible(mid, '0' * 64, alice)
    # Cross-contract execution must be tested against actual StudioNet
    # transactions: the Direct Mode harness uses a single active VM address.


def test_issuer_cannot_change_active_matter(direct_vm, direct_deploy):
    c, _, mid, _, h = create_active(direct_vm,direct_deploy)
    with direct_vm.expect_revert('only matter controller'):
        c.register_actor(mid,actor('charlie'),3)
    c.close_matter(mid)
    assert not c.is_eligible(mid,h,actor('alice'))


def test_public_petitions_require_both_authorities(direct_vm,direct_deploy):
    c, _, mid, _, h = create_active(direct_vm,direct_deploy)
    charlie = actor('charlie')
    with direct_vm.expect_revert('exact frozen authority'):
        with direct_vm.prank(charlie):
            c.file_petition(mid,'https://attacker.com/m', 'https://regulator.example.org/m')
    mock_supported(direct_vm, str(charlie))
    with direct_vm.prank(charlie):
        petition = c.file_petition(mid,'https://service.example.com/m','https://regulator.example.org/m')
    assert c.get_petition(petition)['result'] == 1
    assert c.is_eligible(mid,h,charlie)
    # Validators independently reobserve the two sources; changing either
    # one to remove the frozen claimant anchor must defeat the leader's claim.
    direct_vm.clear_mocks()
    page = f'MAT-100 {charlie} is a paid subscriber who suffered a material service loss.'
    direct_vm.mock_web(r'.*service\.example\.com/m.*', {'status': 200,'body':page})
    direct_vm.mock_web(r'.*regulator\.example\.org/m.*', {'status': 200,'body':'no claimant wallet listed'})
    direct_vm.mock_llm(r'STANDING / PUBLIC MATERIAL-INTEREST ATTESTATION',
        json.dumps({'verdict':'SUPPORTED','quote':page,'reason':'material stake'}))
    assert direct_vm.run_validator() is False


def test_expired_matter_fails_closed(direct_vm,direct_deploy):
    c, _, mid, _, h = create_active(direct_vm,direct_deploy)
    direct_vm.warp(EXPIRED)
    assert not c.is_eligible(mid,h,actor('alice'))


def test_closed_charter_and_public_petitions_disabled(direct_vm,direct_deploy):
    c, _, mid, _, h = create_active(direct_vm,direct_deploy,False)
    with direct_vm.expect_revert('public petitions disabled'):
        with direct_vm.prank(actor('charlie')):
            c.file_petition(mid,'https://service.example.com/m','https://regulator.example.org/m')
    assert c.is_eligible(mid,h,actor('alice'))


def test_registered_dependent_and_cross_matter_hash_are_bound(direct_vm, direct_deploy):
    c, cid, mid, _, h = create_active(
        direct_vm, direct_deploy, extra_actors=[('dependent', 2)])
    assert c.is_eligible(mid, h, actor('dependent'))

    second = c.create_matter(
        cid, 'MAT-200', 'Second matter', 'separate context',
        'service-two.example.com', 'regulator-two.example.org')
    c.register_actor(second, actor('bob'), 3)
    second_hash = c.activate_matter(second, 3600)
    assert not c.is_eligible(mid, second_hash, actor('alice'))
    assert not c.is_eligible(second, h, actor('bob'))


def test_registration_role_duplicate_and_lifetime_guards(direct_vm, direct_deploy):
    direct_vm.warp(BASE)
    c = direct_deploy(CONTRACT)
    cid = c.create_charter('Bounded', 'material interest', 3600, False)
    c.seal_charter(cid)
    mid = c.create_matter(cid, 'MAT-ROLE', 'Role matter', 'context',
                          'service.example.com', 'regulator.example.org')
    c.register_actor(mid, actor('alice'), 2)
    with direct_vm.expect_revert('duplicate actor'):
        c.register_actor(mid, actor('alice'), 3)
    with direct_vm.expect_revert('invalid registered role'):
        c.register_actor(mid, actor('bob'), 1)
    with direct_vm.expect_revert('matter lifetime exceeds charter'):
        c.activate_matter(mid, 3601)
    c.activate_matter(mid, 3600)
    with direct_vm.expect_revert('only matter controller'):
        with direct_vm.prank(actor('bob')):
            c.register_actor(mid, actor('charlie'), 3)


def test_public_petition_wrong_wallet_is_denied(direct_vm, direct_deploy):
    c, _, mid, _, h = create_active(direct_vm, direct_deploy)
    claimant = actor('charlie')
    wrong_wallet = actor('not-charlie')
    page = f'MAT-100 {wrong_wallet} is a paid subscriber with a material service loss.'
    mock_evidence(direct_vm, page, page, json.dumps({
        'verdict': 'SUPPORTED', 'quote': page, 'reason': 'material interest'}))
    with direct_vm.prank(claimant):
        petition = c.file_petition(mid, 'https://service.example.com/m',
                                    'https://regulator.example.org/m')
    assert c.get_petition(petition)['result'] == 2
    assert not c.is_eligible(mid, h, claimant)


def test_single_source_and_ambiguous_model_never_grant(direct_vm, direct_deploy):
    c, _, mid, _, h = create_active(direct_vm, direct_deploy)
    claimant = actor('charlie')
    page = f'MAT-100 {claimant} is a paid subscriber with a material service loss.'
    mock_evidence(direct_vm, page, 'MAT-100 no wallet is listed here', json.dumps({
        'verdict': 'SUPPORTED', 'quote': page, 'reason': 'material interest'}))
    with direct_vm.prank(claimant):
        denied = c.file_petition(mid, 'https://service.example.com/m',
                                 'https://regulator.example.org/m')
    assert c.get_petition(denied)['result'] == 2
    assert not c.is_eligible(mid, h, claimant)

    page_b = f'MAT-100 {claimant} is a paid subscriber with a material service loss.'
    mock_evidence(direct_vm, page, page_b, 'not-json')
    with direct_vm.prank(claimant):
        ambiguous = c.file_petition(mid, 'https://service.example.com/m',
                                    'https://regulator.example.org/m')
    assert c.get_petition(ambiguous)['result'] == 3
    assert not c.is_eligible(mid, h, claimant)


def test_latest_petition_replaces_earlier_public_grant(direct_vm, direct_deploy):
    c, _, mid, _, h = create_active(direct_vm, direct_deploy)
    claimant = actor('charlie')
    page = f'MAT-100 {claimant} is a paid subscriber with a material service loss.'
    mock_supported(direct_vm, str(claimant))
    with direct_vm.prank(claimant):
        first = c.file_petition(mid, 'https://service.example.com/m',
                                'https://regulator.example.org/m')
    assert c.get_petition(first)['result'] == 1
    assert c.is_eligible(mid, h, claimant)

    mock_evidence(direct_vm, 'MAT-100 no claimant wallet listed',
                  'MAT-100 no claimant wallet listed', 'not-json')
    with direct_vm.prank(claimant):
        second = c.file_petition(mid, 'https://service.example.com/m',
                                 'https://regulator.example.org/m')
    assert c.get_petition(second)['result'] == 2
    assert c.get_petition(first)['result'] == 1
    assert not c.is_eligible(mid, h, claimant)


def test_public_attempt_limit_is_bounded(direct_vm, direct_deploy):
    c, _, mid, _, h = create_active(direct_vm, direct_deploy)
    claimant = actor('charlie')
    mock_evidence(direct_vm, 'MAT-100 no claimant wallet listed',
                  'MAT-100 no claimant wallet listed', 'not-json')
    with direct_vm.prank(claimant):
        for _ in range(6):
            petition = c.file_petition(mid, 'https://service.example.com/m',
                                       'https://regulator.example.org/m')
            assert c.get_petition(petition)['result'] == 2
        with direct_vm.expect_revert('attempt limit reached'):
            c.file_petition(mid, 'https://service.example.com/m',
                            'https://regulator.example.org/m')
    assert c.get_attempt_count(mid, claimant) == 6
    assert not c.is_eligible(mid, h, claimant)


def test_public_receipt_expires_before_long_lived_matter(direct_vm, direct_deploy):
    c, _, mid, _, h = create_active(
        direct_vm, direct_deploy, lifetime=10 * 86400, charter_lifetime=10 * 86400)
    claimant = actor('charlie')
    mock_supported(direct_vm, str(claimant))
    with direct_vm.prank(claimant):
        petition = c.file_petition(mid, 'https://service.example.com/m',
                                   'https://regulator.example.org/m')
    assert c.get_petition(petition)['valid_until'] > 0
    assert c.is_eligible(mid, h, claimant)
    direct_vm.warp('2026-10-22T09:00:00+00:00')
    assert not c.is_eligible(mid, h, claimant)

