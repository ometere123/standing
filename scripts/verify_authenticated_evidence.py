"""Prove the authenticated-evidence deployment invariant before value-bearing deploys.

This is intentionally a small, fail-closed gate.  It checks the security-relevant
source structure and then executes the regression tests that exercise the stable
v0.2.12 Direct Mode path.  The deployment script consumes the result; it does not
contain a manually editable VERIFIED switch.
"""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = (ROOT / "contracts" / "standing.py").read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"AUTHENTICATED_EVIDENCE_STATUS=BLOCKED: {message}")


def run_tests(test_path: str, expression: str) -> None:
    env = os.environ.copy()
    env["GENVM_VERSION"] = "v0.2.12"
    command = [
        sys.executable,
        "-m",
        "pytest",
        "-q",
        test_path,
        "-k",
        expression,
    ]
    completed = subprocess.run(command, cwd=ROOT, env=env, text=True)
    require(completed.returncode == 0, f"regression command failed: {' '.join(command)}")


def main() -> int:
    require('class EvidenceCommitment' in CONTRACT, "immutable evidence commitment storage is absent")
    require('def commit_evidence_hash' in CONTRACT, "authority commitment entry point is absent")
    require('only exact configured authority may commit evidence' in CONTRACT,
            "authority sender authentication is absent")
    require('evidence commitment is immutable' in CONTRACT,
            "commitment immutability guard is absent")
    require('keccak(source) != expected_evidence_hash' in CONTRACT,
            "rendered content is not authenticated before semantic assessment")
    require('current_a = observe_once(url_a, reference, wallet, scope, context, expected_hash_a, True)' in CONTRACT,
            "validator does not independently re-fetch source A with its commitment")
    require('current_b = observe_once(url_b, reference, wallet, scope, context, expected_hash_b, True)' in CONTRACT,
            "validator does not independently re-fetch source B with its commitment")
    require('keccak(fresh) != expected_hash' in CONTRACT,
            "validator does not independently recheck the content hash")
    require('gl.nondet.web.get' not in CONTRACT,
            "unsafe web.get evidence path was introduced")
    require("REDIRECT_POLICY_STATUS='UNRESOLVED'" not in
            (ROOT / "scripts" / "deploy_studionet.sh").read_text(encoding="utf-8"),
            "legacy unresolved redirect switch remains in deployment path")

    run_tests("tests/offline/test_primitives.py",
              "authenticated or redirect or source_size or validator")
    run_tests("tests/direct/test_standing_direct.py",
              "authenticated or redirect or missing_commitment or public_petitions_require")
    print("AUTHENTICATED_EVIDENCE_STATUS=VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
