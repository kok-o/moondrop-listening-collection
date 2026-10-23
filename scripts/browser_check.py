from playwright.sync_api import sync_playwright
from pathlib import Path
import json
Path('screenshots').mkdir(exist_ok=True)
with sync_playwright() as p:
 b=p.chromium.launch(channel='chrome',headless=True)
 page=b.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
 errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://localhost:3000',wait_until='networkidle')
 page.evaluate('document.fonts.ready')
 page.screenshot(path='screenshots/desktop-hero.png')
 print(json.dumps({'title':page.title(),'errors':errors,'scrollWidth':page.evaluate('document.documentElement.scrollWidth'),'images':page.locator('img').count(),'buttons':page.get_by_role('button').all_text_contents()},ensure_ascii=True))
 page.screenshot(path='screenshots/desktop-full.png',full_page=True)
 b.close()
