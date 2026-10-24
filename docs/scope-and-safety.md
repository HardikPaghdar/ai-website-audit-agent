# Scope and safety

The demo checks a single HTML page and refuses redirects. Its URL validation is deliberately limited and is not a complete SSRF defense: DNS rebinding, unusual host forms and network-layer routing require additional controls. Before offering a hosted service, resolve and validate all addresses, re-check redirect targets, block private/reserved ranges at egress, cap response sizes, rate-limit callers and isolate network access.

Findings are heuristics, not SEO, performance or accessibility certification. Validate with specialist tools and human review.
