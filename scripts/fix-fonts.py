import requests,re
from pathlib import Path
h=requests.get('https://moondroplab.com/en/brand-toolkit').text
for u in re.findall(r'href="([^"]+)"',h):
 if 'download' in u: print(u)
# inline self-hosted fonts; public CSS imports are not module imports
p=Path('src/app/globals.css');s=p.read_text(encoding='utf-8');s=s.replace("@import url('/assets/manrope.css');\n@import url('/assets/oswald.css');\n",'');s=s.replace("@import 'tailwindcss';", "@import 'tailwindcss';\n"+Path('public/assets/manrope.css').read_text()+Path('public/assets/oswald.css').read_text());p.write_text(s,encoding='utf-8')
