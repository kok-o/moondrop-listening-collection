from playwright.sync_api import sync_playwright,expect
from pathlib import Path
import json,os
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'screenshots';OUT.mkdir(exist_ok=True)
results=[]
with sync_playwright() as p:
 browser=p.chromium.launch(channel='chrome',headless=True)
 for width,height in [(1440,1000),(768,1024),(390,844)]:
  page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
  errors=[];warnings=[];failures=[]
  page.on('pageerror',lambda e:errors.append(str(e)))
  page.on('console',lambda m:warnings.append(m.text) if m.type in ['error','warning'] else None)
  page.on('response',lambda r:failures.append({'url':r.url,'status':r.status}) if r.status>=400 else None)
  page.goto(os.getenv('SITE_URL','http://localhost:3000'),wait_until='networkidle')
  page.evaluate('document.fonts.ready');page.wait_for_timeout(1400)
  expect(page.get_by_role('heading',name='Между звуком и чувством.')).to_be_visible()
  page.screenshot(path=str(OUT/f'{width}-hero.png'))
  page.keyboard.press('Tab');expect(page.locator('.skip-link')).to_be_focused();page.evaluate('document.activeElement.blur()')
  if width==1440:
   page.evaluate('window.scrollTo(0,document.querySelector(".hero-stage").offsetHeight-innerHeight)');page.wait_for_timeout(1400);page.screenshot(path=str(OUT/'1440-transition.png'))
   assert page.locator('.handoff-copy').evaluate('(el)=>parseFloat(getComputedStyle(el).opacity)')>.95
   page.evaluate('window.scrollTo(0,0)');page.wait_for_timeout(1200)
  page.get_by_role('link',name='Открыть коллекцию',exact=True).click();page.wait_for_timeout(1600)
  assert page.evaluate('Math.abs(document.querySelector("#collection").getBoundingClientRect().top)')<180
  for index,section in enumerate(['collection','sound','compare']):
   page.evaluate('(id)=>window.scrollTo(0,document.getElementById(id).offsetTop-25)',section);page.wait_for_timeout(850)
   images=page.locator(f'#{section} img')
   for im in images.all():
    im.scroll_into_view_if_needed();im.evaluate('(img)=>img.decode()')
   page.evaluate('(id)=>window.scrollTo(0,document.getElementById(id).offsetTop-25)',section);page.wait_for_timeout(850)
   page.screenshot(path=str(OUT/f'{width}-{section}.png'))
  for name in ['SPACE TRAVEL','DUSK','COSMO']:
   trigger=page.get_by_role('button',name='Подробнее о '+name,exact=True)
   trigger.click();dialog=page.get_by_role('dialog');expect(dialog).to_be_visible();expect(dialog.get_by_role('heading',name=name,exact=True)).to_be_visible()
   expect(dialog.get_by_role('link',name='На официальный сайт')).to_have_attribute('target','_blank')
   for i in range(5):
    page.keyboard.press('Tab');assert page.evaluate('!!document.activeElement.closest("[role=dialog]")')
   assert dialog.evaluate('(e)=>e.scrollWidth<=e.clientWidth+1')
   if name=='COSMO':
    page.wait_for_timeout(300);page.screenshot(path=str(OUT/f'{width}-dialog.png'))
   page.keyboard.press('Escape');expect(dialog).not_to_be_visible();expect(trigger).to_be_focused()
  sound=page.get_by_role('button',name='Включить атмосферу',exact=False)
  sound.click();expect(page.get_by_role('button',name='Выключить атмосферу',exact=False)).to_have_attribute('aria-pressed','true')
  page.get_by_role('button',name='Выключить атмосферу',exact=False).click();expect(sound).to_have_attribute('aria-pressed','false')
  for link in page.locator('.official-link').all():
   assert link.get_attribute('href').startswith('https://moondroplab.com/en/products/')
  assert page.evaluate('document.documentElement.scrollWidth<=window.innerWidth')
  # Load all lazy images before a full-page screenshot.
  for im in page.locator('img').all():
   im.scroll_into_view_if_needed();im.evaluate('(img)=>img.decode()')
  page.evaluate('window.scrollTo(0,0)');page.wait_for_timeout(1400)
  assert page.locator('.hero-scene').evaluate('(e)=>e.scrollTop===0&&e.scrollLeft===0')
  assert page.locator('.hero-copy').evaluate('(e)=>parseFloat(getComputedStyle(e).opacity)')>.99
  assert page.locator('.yuki-art').evaluate('(e)=>parseFloat(getComputedStyle(e).opacity)')>.99
  page.screenshot(path=str(OUT/f'{width}-returned-to-top.png'))
  broken=page.locator('img').evaluate_all('(imgs)=>imgs.filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src)')
  assert not broken,broken
  assert not errors,errors
  results.append({'width':width,'height':height,'overflow':False,'pageErrors':errors,'console':warnings,'httpErrors':failures,'dialogs':'3 passed, focus trapped, escape and restoration passed','audio':'manual toggle passed','images':'all decoded','anchors':'passed'})
  page.close()
 for width in [1440,390]:
  page=browser.new_page(viewport={'width':width,'height':900},reduced_motion='reduce')
  page.goto(os.getenv('SITE_URL','http://localhost:3000'),wait_until='networkidle');page.wait_for_timeout(300)
  assert not page.locator('html').evaluate('(e)=>e.classList.contains("lenis")')
  assert page.locator('.hero-scene').evaluate('(e)=>e.scrollTop===0&&e.scrollLeft===0')
  assert page.locator('.hero-copy').evaluate('(e)=>getComputedStyle(e).opacity')=='1'
  assert page.locator('.hero-stage').evaluate('(e)=>e.offsetHeight')<1100
  page.screenshot(path=str(OUT/f'{width}-reduced-motion.png'))
  results.append({'width':width,'reducedMotion':'passed: no Lenis, no long pinned section, hero visible'})
  page.close()
 browser.close()
(ROOT/'research/browser-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(results,ensure_ascii=True,indent=2))
