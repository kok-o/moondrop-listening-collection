import requests
from pathlib import Path
from PIL import Image
from io import BytesIO
for n,u in [('yuki','https://cdn.prod.website-files.com/627128d862c9a44234848dda/673aaa0c82767acb2d42c5c6_COSMO-B.jpg'),('cosmo-banner','https://cdn.prod.website-files.com/625fb843a8046c1c7861d89e/6629f584b3e0e6dc4c3bab82_COSMO-M.jpg')]:
 r=requests.get(u);r.raise_for_status();Path('research/'+n+'.jpg').write_bytes(r.content);im=Image.open(BytesIO(r.content)); print(n,im.size);im.thumbnail((850,1100));im.save('research/'+n+'-preview.jpg')
