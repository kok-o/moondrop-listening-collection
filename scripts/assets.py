import requests,json,re,concurrent.futures
from pathlib import Path
from PIL import Image
p=json.loads(Path('research/images.json').read_text())
for name in ['cosmo','dusk','space-travel']:
 im=Image.open('research/'+name+'-0.jpg'); im.save('public/assets/'+name+'.webp',quality=90,method=6)
im=Image.open('research/yuki.jpg'); im.thumbnail((1600,1600));im.save('public/assets/yuki-cosmo.webp',quality=88,method=6)
im=Image.open('research/cosmo-banner.jpg'); im.save('public/assets/cosmo-detail.webp',quality=88,method=6)
im=Image.open('research/cosmo-8.jpg');im.crop((0,0,790,830)).save('public/assets/cosmo-dark.webp',quality=88,method=6)
u=next(u for u in p['home'] if u.endswith('_logo.svg'));r=requests.get(u);Path('public/assets/logo.svg').write_bytes(r.content)
# self-host the actual Google Fonts CSS and files, including Cyrillic
for fam,file in [('Manrope:wght@400;500;600;700;800','manrope'),('Oswald:wght@500;600','oswald')]:
 css=requests.get('https://fonts.googleapis.com/css2?family='+fam+'&display=swap',headers={'User-Agent':'Mozilla/5.0'}).text
 for i,u in enumerate(dict.fromkeys(re.findall(r'url\((https://[^)]+)\)',css))):
  r=requests.get(u);r.raise_for_status();out='/assets/'+file+'-'+str(i)+'.woff2';Path('public'+out).write_bytes(r.content);css=css.replace(u,out)
 Path('public/assets/'+file+'.css').write_text(css)
print('Assets optimized and fonts downloaded')
