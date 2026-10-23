from pathlib import Path
p=Path('scripts/verify_site.py');s=p.read_text(encoding='utf-8').replace("page.keyboard.press('Tab');expect(page.locator('.skip-link')).to_be_focused()", "page.keyboard.press('Tab');expect(page.locator('.skip-link')).to_be_focused();page.evaluate('document.activeElement.blur()')")
s=s.replace("page.screenshot(path=str(OUT/f'{width}-full.png'),full_page=True)", "assert page.locator('.hero-copy').evaluate('(e)=>parseFloat(getComputedStyle(e).opacity)')>.99\n  assert page.locator('.yuki-art').evaluate('(e)=>parseFloat(getComputedStyle(e).opacity)')>.99\n  page.screenshot(path=str(OUT/f'{width}-returned-to-top.png'))")
p.write_text(s,encoding='utf-8')
