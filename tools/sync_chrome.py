"""Refresh shared static navigation/footer. Run from any directory with Python 3."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
EMAIL = 'mailto:youknowitsmestudios@gmail.com'

def identity(base):
    return f'<a class="wordmark" href="{base}" aria-label="You Know Its Me Studios home"><img src="{base}assets/studio-logo.png" width="30" height="30" alt=""><span>You Know Its Me <b>Studios</b></span></a>'

def header(base, route):
    links = [('Projects', '#projects'), ('Strata', 'strata/'), ('Body Hub', 'bodyhub/'), ('About', '#about')]
    nav = ''.join(f'<a href="{base}{url}"' + (' aria-current="page"' if route == url + 'index.html' else '') + f'>{label}</a>' for label, url in links)
    return f'''<header class="site-header"><div class="shell site-header__inner">
{identity(base)}
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-navigation" hidden>Menu</button>
<nav class="site-nav" id="site-navigation" aria-label="Primary navigation">{nav}<a class="contact-link" href="{EMAIL}">Get in touch <img src="{base}assets/icons/arrow-right.svg" alt="" width="20" height="20"></a></nav>
</div></header>'''

def footer(base):
    return f'''<footer class="site-footer"><div class="shell footer-main">
{identity(base)}
<nav aria-label="Footer navigation"><a href="{base}#projects">Projects</a><a href="{base}strata/">Strata</a><a href="{base}bodyhub/">Body Hub</a><a href="{base}#about">About</a><a href="{EMAIL}">Contact</a></nav>
<div class="footer-social"><a href="https://github.com/You-Know-Its-Me-Studios/youknowitsmestudios" aria-label="Studio on GitHub"><img src="{base}assets/icons/brand-github.svg" alt="" width="20" height="20"></a><a href="{EMAIL}" aria-label="Email the studio"><img src="{base}assets/icons/mail.svg" alt="" width="20" height="20"></a></div>
<p class="footer-motto">Small ideas<br>Bigger tomorrows</p>
</div><div class="shell footer-resources"><p>© <span data-current-year>2026</span> You Know Its Me Studios</p><nav aria-label="Support and legal"><a href="{base}support/strata/">Strata support</a><a href="{base}privacy/strata/">Strata privacy policy</a><a href="{base}bodyhub/support.html">Body Hub support</a><a href="{base}bodyhub/privacy.html">Body Hub privacy policy</a><a href="{base}bodyhub/terms.html">Body Hub terms of use</a><a href="{base}bodyhub/data-deletion.html">Body Hub data &amp; deletion</a></nav></div></footer>'''

def sync():
    for page in ROOT.rglob('*.html'):
        route = page.relative_to(ROOT).as_posix()
        base = '../' * (len(Path(route).parts) - 1) or './'
        text = page.read_text(encoding='utf-8')
        text = re.sub(r'<link\b[^>]*\brel="icon"[^>]*>', lambda _: f'<link rel="icon" href="{base}assets/studio-logo.png" type="image/png">', text)
        text = re.sub(r'<header class="site-header".*?</header>', lambda _: header(base, route), text, flags=re.S)
        text = re.sub(r'<footer class="site-footer".*?</footer>', lambda _: footer(base), text, flags=re.S)
        text = re.sub(r'styles.css\?v=[^"\s]+', 'styles.css?v=20261003-4', text)
        text = re.sub(r'script.js(?:\?v=[^"\s]+)?', 'script.js?v=20261003-4', text)
        text = text.replace('content="#090b0d"', 'content="#080e12"')
        if route.startswith('bodyhub/'):
            text = text.replace('<body>', '<body class="theme-bodyhub">')
        page.write_text(text, encoding='utf-8')

if __name__ == '__main__':
    sync()
