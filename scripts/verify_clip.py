from pathlib import Path
p=Path('scripts/verify_site.py');s=p.read_text(encoding='utf-8').replace("assert page.locator('.hero-copy').evaluate", "assert page.locator('.hero-scene').evaluate('(e)=>e.scrollTop===0&&e.scrollLeft===0')\n  assert page.locator('.hero-copy').evaluate");p.write_text(s,encoding='utf-8')
