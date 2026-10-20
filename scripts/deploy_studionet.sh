#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
CLI='./node_modules/.bin/genlayer'
RPC='https://studio.genlayer.com/api'
CLI_MODE='posix'
if ! command -v node >/dev/null 2>&1 && command -v node.exe >/dev/null 2>&1 && [[ -f "$CLI.cmd" ]]; then
  # WSL/bash on Windows cannot execute a .cmd file as a shell script; use the
  # Windows command interpreter while still selecting the repository-local CLI.
  CLI="$CLI.cmd"
  CLI_MODE='windows'
fi
if [[ ! -f "$CLI" ]] || [[ "$CLI_MODE" == 'posix' && ! -x "$CLI" ]]; then
  echo 'ERROR: install repository-local genlayer@0.39.1 first' >&2
  exit 11
fi
run_cli() {
  if [[ "$CLI_MODE" == 'windows' ]]; then
    cmd.exe /d /c ".\\node_modules\\.bin\\genlayer.cmd $*"
  else
    "$CLI" "$@"
  fi
}
VERSION="$(run_cli --version 2>&1)"
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
run_cli network set studionet
run_cli network info
"$PYTHON_BIN" scripts/verify_studionet.py
printf '\nPreflight verified: studionet / chain 61999 / %s\n' "$RPC"
printf 'Deploying MAIN Standing (no other network will be attempted)\n'
run_cli deploy --contract contracts/standing.py
printf '\nSTOP: record and verify finalized successful main contract address before consumer deployment.\n'
printf 'Do not deploy consumer with any guessed address. Follow docs/CODEX_HANDOFF.md.\n'
