from playwright.sync_api import sync_playwright,expect
from pathlib import Path
import json
url='https://moondrop-listening-collection.vercel.app'
results=[]
with sync_playwright() as p:
 browser=p.chromium.launch(channel='chrome',headless=True)
 for width,height in [(1440,1000),(390,844)]:
  page=browser.new_page(viewport={'width':width,'height':height})
  errors=[];bad=[]
  page.on('pageerror',lambda e:errors.append(str(e)))
  page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None)
  page.on('response',lambda r:bad.append({'url':r.url,'status':r.status}) if r.status>=400 else None)
  response=page.goto(url,wait_until='networkidle',timeout=60000);page.evaluate('document.fonts.ready');page.wait_for_timeout(1400)
  expect(page.get_by_role('heading',name='Между звуком и чувством.')).to_be_visible()
  page.screenshot(path=f'screenshots/vercel-{width}.png')
  page.get_by_role('link',name='Открыть коллекцию',exact=True).click();page.wait_for_timeout(1500)
  for model in ['SPACE TRAVEL','DUSK','COSMO']:
   page.get_by_role('button',name='Подробнее о '+model,exact=True).click();expect(page.get_by_role('dialog')).to_be_visible();expect(page.get_by_role('dialog').get_by_role('heading',name=model,exact=True)).to_be_visible();page.keyboard.press('Escape')
  for im in page.locator('img').all():
   im.scroll_into_view_if_needed();im.evaluate('(i)=>i.decode()')
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
  assert not errors,errors
  assert not bad,bad
  results.append({'width':width,'status':response.status,'url':page.url,'title':page.title(),'pageAndConsoleErrors':errors,'httpErrors':bad,'allImagesDecoded':True,'dialogs':'all 3 passed','overflow':False})
  page.close()
 browser.close()
Path('research/vercel-verification.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(results,ensure_ascii=True,indent=2))
