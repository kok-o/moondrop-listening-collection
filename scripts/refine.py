from pathlib import Path
for n in ['cosmo','dusk','space-travel']:
 Path('public/assets/'+n+'.webp').rename('public/assets/'+n+'-cutout.webp')
Path('public/assets/yuki-cosmo.webp').rename('public/assets/yuki-cosmo-ink.webp')
for f in ['src/app/page.tsx','src/lib/products.ts','scripts/sources.py','SOURCES.md','public/sources.html']:
 p=Path(f);s=p.read_text(encoding='utf-8')
 for n in ['cosmo','dusk','space-travel']:s=s.replace(n+'.webp',n+'-cutout.webp')
 s=s.replace('yuki-cosmo.webp','yuki-cosmo-ink.webp');p.write_text(s,encoding='utf-8')
p=Path('scripts/transparent_assets.py');s=p.read_text();s=s.replace("name+'.webp'","name+'-cutout.webp'").replace('yuki-cosmo.webp','yuki-cosmo-ink.webp');p.write_text(s)
p=Path('src/app/globals.css');s=p.read_text();s+='\n@media(min-width:901px){.hero-copy{animation-fill-mode:backwards}}\n';p.write_text(s)
p=Path('scripts/verify_site.py');s=p.read_text(encoding='utf-8').replace("page.evaluate('window.scrollTo(0,700)')","page.evaluate('window.scrollTo(0,document.querySelector(\".hero-stage\").offsetHeight-innerHeight)')");p.write_text(s,encoding='utf-8')
