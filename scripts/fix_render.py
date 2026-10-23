from pathlib import Path
for f in ['src/app/page.tsx','src/lib/products.ts','scripts/sources.py','SOURCES.md','public/sources.html']:
 p=Path(f);s=p.read_text(encoding='utf-8').replace('yuki-cosmo-cutout.webp','yuki-cosmo-ink.webp');p.write_text(s,encoding='utf-8')
p=Path('src/components/MotionDirector.tsx');s=p.read_text(encoding='utf-8').replace('anchors: {offset: -82}','anchors: true');p.write_text(s,encoding='utf-8')
p=Path('src/app/globals.css');s=p.read_text();s+='\nhtml{scroll-padding-top:0}.brand img,.site-footer .brand img{height:auto}\n';p.write_text(s)
