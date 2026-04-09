# VERIFRAX-API

Canonical API source for `api.verifrax.net`.

Execution surface only.

[![Contract Status](https://github.com/Verifrax/VERIFRAX-API/actions/workflows/contract-status.yml/badge.svg?branch=main)](https://github.com/Verifrax/VERIFRAX-API/actions/workflows/contract-status.yml)
[![contract](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Verifrax/VERIFRAX-API/main/badges/contract.json)](https://github.com/Verifrax/VERIFRAX-API/blob/main/evidence/current/contract-status.json)
[![healthz](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Verifrax/VERIFRAX-API/main/badges/healthz.json)](https://api.verifrax.net/healthz)
[![readyz](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Verifrax/VERIFRAX-API/main/badges/readyz.json)](https://api.verifrax.net/readyz)
[![version](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Verifrax/VERIFRAX-API/main/badges/version.json)](https://api.verifrax.net/version)
[![openapi](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Verifrax/VERIFRAX-API/main/badges/openapi.json)](https://api.verifrax.net/openapi.json)

## Current contract status

Current contract status: `/healthz`, `/readyz`, `/version`, and `/openapi.json` are live on the current host binding.

Evidence source:
- `evidence/current/contract-status.json`

Public contract endpoints:
- `https://api.verifrax.net/healthz`
- `https://api.verifrax.net/readyz`
- `https://api.verifrax.net/version`
- `https://api.verifrax.net/openapi.json`

Governed projection endpoints:
- `https://api.verifrax.net/api/capabilities`
- `https://api.verifrax.net/api/law`
- `https://api.verifrax.net/api/state`
- `https://api.verifrax.net/api/receipt/example-0001`
- `https://api.verifrax.net/api/verdict/example-0001`

## Boundary

VERIFRAX-SURFACE controls form.
Host-owning repositories control function and content.



- source-of-truth repo for the execution host
- deployment target is Cloudflare Worker / edge runtime
- `api.verifrax.net` must remain bound to execution infrastructure
- root HTML is informational only and does not outrank the live contract endpoints
- README badges are projections of probe-generated evidence, not assertions by prose

## Truth rule

No surface in this repository may claim liveness or readiness unless that claim is derived from a reproducible live probe.

`README.md` is projection.  
`index.html` is projection.  
`badges/*.json` are projection.  
`evidence/current/contract-status.json` is the machine-readable contract evidence.

## Governed verification direction

This repository is the execution-surface anchor for a future end-to-end governed verification system:

- SYNTAGMARIUM defines law
- ORBISTIUM holds accepted state
- CONSONORIUM reconciles runtime/state
- VERIFRAX-API exposes execution-surface contract truth for `api.verifrax.net`

## License

Apache License Version 2.0

## Validation

```bash
python3 scripts/contract_probe.py
python3 -m json.tool evidence/current/contract-status.json >/dev/null
python3 -m json.tool badges/healthz.json >/dev/null
python3 -m json.tool badges/readyz.json >/dev/null
python3 -m json.tool badges/version.json >/dev/null
python3 -m json.tool badges/openapi.json >/dev/null
python3 -m json.tool badges/contract.json >/dev/null
````

