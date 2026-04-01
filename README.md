# VERIFRAX-API

Canonical API source for api.verifrax.net.

Execution surface only.

## Boundary
- source-of-truth repo for the execution host
- deployment target is Cloudflare Worker / edge runtime
- no GitHub Pages publication
- no public CNAME binding to github.io
- api.verifrax.net must remain bound to execution infrastructure, not a static Pages host
