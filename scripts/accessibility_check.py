from pathlib import Path
import requests
r=requests.get('https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.3/axe.min.js');r.raise_for_status();Path('research/axe.min.js').write_text(r.text,encoding='utf-8')
from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
 b=p.chromium.launch(channel='chrome',headless=True);page=b.new_page(viewport={'width':1440,'height':1000});page.goto('http://localhost:3000',wait_until='networkidle');page.wait_for_timeout(1300);page.add_script_tag(path='research/axe.min.js')
 results=page.evaluate('''async()=>{const r=await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa']}});return r.violations.map(v=>({id:v.id,impact:v.impact,description:v.description,nodes:v.nodes.map(n=>({html:n.html,summary:n.failureSummary}))}))}''')
 Path('research/accessibility-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(results,ensure_ascii=True));b.close()

