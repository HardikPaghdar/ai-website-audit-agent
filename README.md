# AI Website Audit Agent

Rule-based audit for public HTML pages. Checks title/description, canonical, H1 structure, image alt attributes, generic link labels and noindex signals. Outputs actionable findings in JSON and Markdown.

## Run
`pip install -r requirements.txt`
`python -m website_audit.cli https://example.com --out reports/audit.md`
`pytest`

This is not a Lighthouse/Core Web Vitals report, WCAG certification, JavaScript crawler or AI-search ranking guarantee. Only audit sites you are authorized to test. Basic URL guards are not a complete SSRF defense; see docs.
