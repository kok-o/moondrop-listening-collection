from pathlib import Path
from PIL import Image,ImageDraw,ImageChops
im=Image.open('research/cosmo-0.jpg').convert('RGB');r,g,b=im.split();candidate=ImageChops.darker(ImageChops.darker(r,g),b).point(lambda v:255 if v>244 else 0)
for seed in [(0,0),(250,50),(250,175)]:
 if candidate.getpixel(seed)==255:ImageDraw.floodfill(candidate,seed,128,thresh=0)
im.putalpha(candidate.point(lambda v:0 if v==128 else 255));im.save('public/assets/cosmo-render.webp',quality=92,method=6)
for f in ['src/app/page.tsx','src/lib/products.ts','scripts/sources.py','SOURCES.md','public/sources.html']:
 p=Path(f);s=p.read_text(encoding='utf-8').replace('cosmo-cutout.webp','cosmo-render.webp');p.write_text(s,encoding='utf-8')
