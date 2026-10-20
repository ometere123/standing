"""Fail-closed RPC verification; do NOT interpret unavailable chain ID as 61999."""
import json
import urllib.request
import sys

RPC = 'https://studio.genlayer.com/api'
EXPECTED = 61999


def rpc(method: str):
    body = json.dumps({'jsonrpc':'2.0','id':1,'method':method,'params':[]}).encode()
    req = urllib.request.Request(
        RPC,
        data=body,
        headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'standing-studionet-guard/1.0',
        },
        method='POST',
    )
    with urllib.request.urlopen(req, timeout=15) as response:
        data=json.loads(response.read(65536).decode('utf-8'))
    if data.get('error') is not None or 'result' not in data:
        raise ValueError(f'RPC method {method} did not give result: {data.get("error")}')
    return data['result']


def parse_id(x):
    if isinstance(x,int): return x
    if isinstance(x,str) and x.startswith('0x'): return int(x,16)
    if isinstance(x,str) and x.isdigit(): return int(x)
    raise ValueError('Unrecognized chain ID response')


def verify():
    errors=[]
    for method in ('eth_chainId', 'net_version'):
        try:
            actual=parse_id(rpc(method))
        except Exception as e:
            errors.append(f'{method}: {e}')
            continue
        if actual != EXPECTED:
            raise RuntimeError(f'FATAL WRONG CHAIN {actual}, expected {EXPECTED}; no deployment')
        print(f'VALIDATED {method} = {EXPECTED}, RPC={RPC}')
        return True
    raise RuntimeError('Could not independently verify 61999 via RPC; fail closed. '+ '; '.join(errors))

if __name__=='__main__':
    try: verify()
    except Exception as e:
        print(f'STOP: {e}',file=sys.stderr)
        raise SystemExit(13)
