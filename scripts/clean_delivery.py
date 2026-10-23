from pathlib import Path
p=Path('package.json');import json;data=json.loads(p.read_text());data['license']='UNLICENSED';p.write_text(json.dumps(data,indent=2)+'\n')
p=Path('package-lock.json');data=json.loads(p.read_text());data['packages']['']['license']='UNLICENSED';p.write_text(json.dumps(data,indent=2)+'\n')
# Discard superseded diagnostic screenshots; keep the final width-specific captures.
for f in ['desktop-hero.png','desktop-full.png','anchor-debug.png','1440-full.png','768-full.png','390-full.png']:
 p=Path('screenshots')/f
 if p.exists():p.unlink()
