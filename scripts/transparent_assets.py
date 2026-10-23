from PIL import Image,ImageChops,ImageDraw
from pathlib import Path
# Remove only edge-connected white studio backdrops, preserving product highlights.
for name in ['cosmo','dusk','space-travel']:
 im=Image.open('research/'+name+'-0.jpg').convert('RGB')
 mask=Image.eval(im.convert('L'),lambda v:255 if v>244 else 0)
 # Background candidate requires all RGB channels to be near white.
 r,g,b=im.split();candidate=ImageChops.darker(ImageChops.darker(r,g),b).point(lambda v:255 if v>244 else 0)
 ImageDraw.floodfill(candidate,(0,0),128,thresh=0)
 alpha=candidate.point(lambda v:0 if v==128 else 255)
 im.putalpha(alpha);im.save('public/assets/'+name+'-cutout.webp',quality=92,method=6)
# Official line art is printed on white; remove paper using its lightest neutral component.
# Recover original ink colors so the illustration composites cleanly on milk/rose.
im=Image.open('research/yuki.jpg').convert('RGB');im.thumbnail((1600,1600));pixels=[]
for r,g,b in im.getdata():
 a=255-min(r,g,b)
 if a<4:pixels.append((0,0,0,0))
 else:pixels.append((int(255*(r-255+a)/a),int(255*(g-255+a)/a),int(255*(b-255+a)/a),a))
out=Image.new('RGBA',im.size);out.putdata(pixels);out.save('public/assets/yuki-cosmo-ink.webp',quality=90,method=6)
print('Transparent optimized assets ready')
