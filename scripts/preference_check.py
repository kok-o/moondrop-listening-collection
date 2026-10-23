from playwright.sync_api import sync_playwright
from pathlib import Path
import json
with sync_playwright() as p:
 b=p.chromium.launch(channel='chrome',headless=True);page=b.new_page(viewport={'width':1440,'height':1000});page.goto('http://localhost:3000',wait_until='networkidle');page.wait_for_timeout(1200)
 page.evaluate('window.scrollTo(0,800)');page.wait_for_timeout(1000);page.emulate_media(reduced_motion='reduce');page.wait_for_timeout(300)
 assert not page.locator('html').evaluate('(e)=>e.classList.contains("lenis")')
 assert page.locator('.hero-copy').evaluate('(e)=>parseFloat(getComputedStyle(e).opacity)')==1
 page.emulate_media(reduced_motion='no-preference');page.wait_for_timeout(600);assert page.locator('html').evaluate('(e)=>e.classList.contains("lenis")')
 page.evaluate('window.scrollTo(0,0)');page.wait_for_timeout(1000)
 page.add_script_tag(path='research/axe.min.js');r=page.evaluate('''async()=>{let r=await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa']}});return r.violations.map(v=>v.id)}''');assert not r,r
 print(json.dumps({'runtimeMotionPreference':'cleanup and reinitialization passed','accessibility':r,'heroOverflow':page.locator('.hero-scene').evaluate('(e)=>getComputedStyle(e).overflow')}));b.close()
