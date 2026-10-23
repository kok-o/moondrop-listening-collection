from playwright.sync_api import sync_playwright
from pathlib import Path
import json
results=[]
with sync_playwright() as p:
 b=p.chromium.launch(channel='chrome',headless=True)
 for width in [1440,390]:
  page=b.new_page(viewport={'width':width,'height':900});page.goto('http://localhost:3000',wait_until='networkidle');page.wait_for_timeout(1200);page.add_script_tag(path='research/axe.min.js')
  for name in ['page','SPACE TRAVEL','DUSK','COSMO']:
   if name!='page':page.get_by_role('button',name='Подробнее о '+name,exact=True).click();page.wait_for_timeout(300)
   violations=page.evaluate('''async()=>{const r=await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa']}});return r.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.html)}))}''')
   results.append({'width':width,'state':name,'violations':violations})
   if name!='page':page.keyboard.press('Escape')
  page.close()
 page=b.new_page();page.goto('http://localhost:3000/sources.html',wait_until='networkidle');assert page.title().startswith('Материалы и источники');assert page.locator('a').count()>10
 b.close()
Path('research/accessibility-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(results,ensure_ascii=True));assert all(not r['violations'] for r in results)
