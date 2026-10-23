from pathlib import Path
p=Path('scripts/verify_site.py');s=p.read_text(encoding='utf-8').replace("if name=='COSMO':page.screenshot(path=str(OUT/f'{width}-dialog.png'))","if name=='COSMO':\n    page.wait_for_timeout(300);page.screenshot(path=str(OUT/f'{width}-dialog.png'))");p.write_text(s,encoding='utf-8')
