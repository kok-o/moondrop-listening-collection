from playwright.sync_api import sync_playwright
with sync_playwright() as p:
 b=p.chromium.launch(channel='chrome',headless=True);page=b.new_page(viewport={'width':1440,'height':1000});page.goto('http://localhost:3000',wait_until='networkidle');page.wait_for_timeout(1500)
 print('BEFORE',page.evaluate('({y:scrollY,collection:document.querySelector("#collection").offsetTop})'))
 page.get_by_role('link',name='Открыть коллекцию',exact=True).click()
 for i in range(5):
  page.wait_for_timeout(700);print('scroll',page.evaluate('({y:scrollY,top:document.querySelector("#collection").getBoundingClientRect().top,hash:location.hash})'))
 page.screenshot(path='screenshots/anchor-debug.png');b.close()
