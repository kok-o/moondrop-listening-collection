from pathlib import Path
import re
h=Path('research/drawing.html').read_text(encoding='utf-8')
for u,t in re.findall(r'href="([^"]+)"[^>]*>(.*?)</a>',h):
 if any(x in t for x in ['COSMO','DUSK','SPACE TRAVEL','VENUS']): print(re.sub('<[^>]*>','',t),u)
h=Path('research/home.html').read_text(encoding='utf-8')
for v in re.findall(r'[^<]{0,120}background-image[^>]{0,350}',h): print(v)
