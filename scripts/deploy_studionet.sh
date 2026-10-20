#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
CLI='./node_modules/.bin/genlayer'
RPC='https://studio.genlayer.com/api'
if [[ ! -x "$CLI" ]]; then echo 'ERROR: install repo-local genlayer@0.39.1 first' >&2; exit 11; fi
VERSION="$($CLI --version 2>&1)"
if [[ "$VERSION" != *'0.39.1'* ]] || [[ "$VERSION" == *'0.40.'* ]]; then
  echo "ERROR: expected repository-local genlayer@0.39.1; observed $VERSION" >&2; exit 12
fi
if [[ -x '.venv/bin/python' ]]; then
  PYTHON_BIN='.venv/bin/python'
elif [[ -x '.venv/Scripts/python.exe' ]]; then
  PYTHON_BIN='.venv/Scripts/python.exe'
else
  PYTHON_BIN='python'
fi
"$PYTHON_BIN" scripts/static_preflight.py
AUTH_PROOF="$("$PYTHON_BIN" scripts/verify_authenticated_evidence.py)"
printf '%s\n' "$AUTH_PROOF"
if [[ "$AUTH_PROOF" != *'AUTHENTICATED_EVIDENCE_STATUS=VERIFIED'* ]]; then
  echo 'BLOCKED: authenticated evidence proof gate did not verify; no value-bearing deployment.' >&2
  exit 14
fi
"$CLI" network set studionet
"$CLI" network info
"$PYTHON_BIN" scripts/verify_studionet.py
printf '\nPreflight verified: studionet / chain 61999 / %s\n' "$RPC"
printf 'Deploying MAIN Standing (no other network will be attempted)\n'
"$CLI" deploy --contract contracts/standing.py
printf '\nSTOP: record and verify finalized successful main contract address before consumer deployment.\n'
printf 'Do not deploy consumer with any guessed address. Follow docs/CODEX_HANDOFF.md.\n'
