from PIL import Image
for n in ['yuki-cosmo','cosmo','dusk','space-travel']:
 i=Image.open('public/assets/'+n+'.webp');print(n,i.mode,i.getpixel((0,0)))
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
 b=p.chromium.launch(channel='chrome',headless=True);page=b.new_page(viewport={'width':1440,'height':1000});page.goto('http://localhost:3000',wait_until='networkidle');page.wait_for_timeout(1500)
 print('before',page.locator('.hero-scene').evaluate('(e)=>({position:getComputedStyle(e).position,top:e.getBoundingClientRect().top,root:document.documentElement.className})'))
 page.evaluate('window.scrollTo(0,820)');page.wait_for_timeout(2000)
 print('after',page.locator('.handoff-copy').evaluate('(e)=>({opacity:getComputedStyle(e).opacity,y:scrollY,transform:document.querySelector(".hero-product").style.transform,root:document.documentElement.className})'))
 print('scripts',page.locator('script[src]').evaluate_all('(e)=>e.map(x=>x.src)'))
 b.close()
