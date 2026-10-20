"""Stable StudioNet GenVM direct-mode environment, not Studio-dev preview."""
import os
from gltest.direct import loader, sdk_loader
from gltest.direct import VMContext

# Stable 61999 contracts use the v0.2.12 GenVM bundle.
# Prevent the direct test package selecting a future/preview runner.
sdk_loader.get_latest_version = lambda: 'v0.2.12'
sdk_loader.list_cached_versions = lambda: ['v0.2.12']

_original_inject = loader._inject_message_to_fd0

def _safe_inject(vm):
    try:
        return _original_inject(vm)
    except PermissionError:
        if os.name != 'nt':
            raise
        return None

loader._inject_message_to_fd0 = _safe_inject

# genlayer-test 0.29.0 refreshes sender/value when the clock is warped, but
# leaves the cached ``gl.message_raw['datetime']`` unchanged.  The contract
# correctly reads the stable runner's transaction datetime from message_raw;
# keep the Direct Mode harness' clock cheatcode aligned with that production
# field so expiry-boundary tests exercise the same path.
_original_warp = VMContext.warp


def _warp_and_refresh_raw(self, timestamp):
    _original_warp(self, timestamp)
    gl_module = __import__('sys').modules.get('genlayer.gl')
    if gl_module is not None and getattr(gl_module, 'message_raw', None) is not None:
        gl_module.message_raw['datetime'] = timestamp


VMContext.warp = _warp_and_refresh_raw
