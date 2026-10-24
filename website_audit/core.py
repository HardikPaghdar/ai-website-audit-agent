from bs4 import BeautifulSoup
def audit_html(html):
 s=BeautifulSoup(html,'html.parser'); out=[]
 def add(level,title,evidence,fix): out.append({'severity':level,'title':title,'evidence':evidence,'recommendation':fix})
 if not s.title or not s.title.get_text(strip=True): add('high','Missing title','No title found','Add a unique page title')
 if not s.find('meta',attrs={'name':'description'}): add('medium','Missing meta description','No description meta tag','Add a concise page summary')
 if not s.find('link',rel='canonical'): add('medium','Missing canonical','No canonical link','Add a canonical URL where appropriate')
 if not s.find('h1'): add('medium','Missing H1','No H1 heading','Add a clear primary heading')
 missing=[i for i in s.find_all('img') if i.get('alt') is None]
 if missing: add('medium','Images missing alt',str(len(missing))+' images','Add meaningful alt text or empty alt for decorative images')
 generic=[a for a in s.find_all('a') if a.get_text(' ',strip=True).lower() in {'click here','here','read more'}]
 if generic: add('low','Generic link labels',str(len(generic))+' links','Use descriptive link text')
 return out or [{'severity':'info','title':'No configured checks triggered','evidence':'No issues detected by current rules','recommendation':'Review manually and run specialist tools'}]
