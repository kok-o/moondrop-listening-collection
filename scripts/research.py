import requests,re,json
from pathlib import Path
pages={}
for name,url in [('home','https://moondroplab.com/en/home'),('cosmo','https://moondroplab.com/en/products/cosmo'),('dusk','https://moondroplab.com/en/products/dusk'),('space-travel','https://moondroplab.com/en/products/space-travel'),('drawing','https://moondroplab.com/en/drawing')]:
 html=requests.get(url,headers={'User-Agent':'Mozilla/5.0'}).text; Path('research/'+name+'.html').write_text(html,encoding='utf-8')
 imgs=list(dict.fromkeys(re.findall(r'<img[^>]+src="([^"]+)"',html)))
 pages[name]=imgs
 print(name, json.dumps(imgs,ensure_ascii=False))
Path('research/images.json').write_text(json.dumps(pages,indent=2),encoding='utf-8')

