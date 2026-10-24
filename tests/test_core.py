from website_audit.core import audit_html

def test_missing_alt_and_description():
 titles={x['title'] for x in audit_html('<html><head><title>Hi</title></head><body><h1>Hi</h1><img src="x"></body></html>')}
 assert 'Images missing alt' in titles and 'Missing meta description' in titles
