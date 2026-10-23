import requests,re,json,concurrent.futures
from pathlib import Path
from PIL import Image,ImageDraw
from io import BytesIO
pages=json.loads(Path('research/images.json').read_text())
urls=[]
for name in ['cosmo','dusk','space-travel']:
 for i,u in enumerate(pages[name][14:-6]): urls.append((name+'-'+str(i),u))
for u in re.findall(r'https://cdn[^"<> )]+',Path('research/home.html').read_text(encoding='utf-8')):
 if any(k in u.lower() for k in ['cosmo','yuki','mitsuki']): print('EXTRA',u)
def get(v):
 name,u=v
 r=requests.get(u);r.raise_for_status();Path('research/'+name+'.jpg').write_bytes(r.content)
 im=Image.open(BytesIO(r.content)); print(name,im.size)
 im.thumbnail((240,220));return name,im.copy()
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex: ims=list(ex.map(get,urls))
sheet=Image.new('RGB',(1200,((len(ims)+4)//5)*250),'#eeeeee');d=ImageDraw.Draw(sheet)
for i,(n,im) in enumerate(ims): x=(i%5)*240;y=(i//5)*250;sheet.paste(im,(x,y));d.text((x+5,y+225),n,fill='black')
sheet.save('research/contact.jpg')
# drawing originals use links instead of image tags
html=Path('research/drawing.html').read_text(encoding='utf-8')
links=re.findall(r'href="([^"]+)"[^>]*>(.*?)</a>',html)
for u,t in links:
 if 'COSMO' in t or 'DUSK' in t or 'SPACE TRAVEL' in t: print('ART',re.sub('<[^>]*>','',t),u)
