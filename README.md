# AI Website Audit Agent

Rule-based audit of public HTML for titles, descriptions, canonical links, H1 structure, missing image alt text and generic link labels. Outputs findings with fixes; not a Lighthouse, WCAG certification, or AI-search ranking tool.

Run: `pip install -r requirements.txt`; `python -m website_audit.cli https://example.com`; `pytest`. Only audit sites you are authorized to test. URL guards are demo-level, not complete SSRF protection.
