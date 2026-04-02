# VERIFRAX-API

Canonical repository for `api.verifrax.net`.

## Status

- Repository role: API host implementation surface
- Public host ownership: `https://api.verifrax.net/`
- Current live host binding: static GitHub Pages-backed boundary page on the custom domain
- Current contract status: `/healthz`, `/readyz`, `/version`, and `/openapi.json` are not live on the current host binding
- Implementation status: `wrangler.toml` and Worker-oriented runtime material exist in the repository, but they are not the current live host truth
- Package status: repository-private root workspace
- License: Apache License Version 2.0

## One-sentence role

`VERIFRAX-API` is the host-owning implementation repository for `api.verifrax.net`, and it must describe the live API host truth exactly without overstating contract availability or runtime deployment state.

## What this repository is

This repository exists to hold:

- API-host implementation material
- host boundary metadata
- contract-facing implementation files when they are truly live
- deployment-facing runtime configuration
- API-surface validation and projection rules

## What this repository is not

This repository is not:

- the proof publication surface
- the public verifier surface
- the authority issuance surface
- the runtime reference surface
- the intake surface
- the docs surface
- the status surface
- the commercial root surface

It is also not allowed to claim:

- a live Worker deployment when the host is serving from GitHub Pages
- live contract endpoints when those endpoints return `404`
- proof, verification, intake, docs, or status ownership

## Current live boundary

The current live root at `https://api.verifrax.net/` serves a static boundary page.

That current live host truth means:

- the root host is reachable
- the custom domain is live
- the current host is not yet serving the declared machine contract paths
- repository truth must follow that current host state until deployment truth changes

## Contract boundary

The intended API contract includes these paths:

- `/healthz`
- `/readyz`
- `/version`
- `/openapi.json`

Those paths must not be described here as live contract surfaces until the live host actually serves them successfully.

## Implementation boundary

This repository contains Worker-oriented implementation material, including `wrangler.toml`.

That implementation material is retained as repository implementation surface.

It must not be confused with current live deployment truth unless the live host binding and contract responses actually match it.

## Adjacent surfaces

- `https://proof.verifrax.net/` — proof publication
- `https://verify.verifrax.net/` — public verification
- `https://auctoriseal.verifrax.net/` — authority issuance/reference
- `https://corpiform.verifrax.net/` — runtime reference
- `https://apply.verifrax.net/` — intake
- `https://docs.verifrax.net/` — documentation
- `https://status.verifrax.net/` — operational status
- `https://www.verifrax.net/` — commercial root

## Reading rule

Read this repository as the API host implementation boundary only.

Do not read it as proof, verifier, authority, intake, docs, status, or commercial truth.

Do not read runtime implementation intent as equivalent to current live host state.

## License

Apache License Version 2.0
