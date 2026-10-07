"""Check the static site at its GitHub Pages project path; no dependencies."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://you-know-its-me-studios.github.io/youknowitsmestudios/'


class Page(HTMLParser):
    def __init__(self, content):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.references = []
        self.links = []
        self.active_link = None
        self.errors = []
        self.feed(content)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for attr in ('href', 'src', 'poster'):
            if attr in attrs:
                self.references.append(attrs[attr])
        if tag == 'img' and 'alt' not in attrs:
            self.errors.append('Image without alt text')
        if tag == 'a':
            self.active_link = [attrs.get('href', ''), attrs.get('aria-label', '')]

    def handle_data(self, data):
        if self.active_link is not None:
            self.active_link[1] += data

    def handle_endtag(self, tag):
        if tag == 'a' and self.active_link is not None:
            self.links.append(self.active_link)
            self.active_link = None


def check():
    pages = {p.relative_to(ROOT).as_posix(): Page(p.read_text(encoding='utf-8'))
             for p in ROOT.rglob('*.html')}
    errors = []
    references = 0

    def check_url(route, reference):
        nonlocal references
        references += 1
        if not reference or reference == '#' or reference.startswith(('mailto:', 'javascript:', '/')):
            errors.append(f'{route}: unwanted destination {reference!r}')
            return
        target = urlsplit(urljoin(BASE + route, reference))
        if target.netloc != urlsplit(BASE).netloc:
            return
        prefix = urlsplit(BASE).path
        if not target.path.startswith(prefix):
            errors.append(f'{route}: leaves the project path: {reference}')
            return
        relative = unquote(target.path[len(prefix):])
        path = ROOT / relative
        if path.is_dir():
            path = path / 'index.html'
        if not path.is_file():
            errors.append(f'{route}: missing {reference}')
            return
        resolved = path.relative_to(ROOT).as_posix()
        if target.fragment and resolved in pages and unquote(target.fragment) not in pages[resolved].ids:
            errors.append(f'{route}: missing fragment {reference}')

    for route, page in pages.items():
        errors.extend(f'{route}: {error}' for error in page.errors)
        errors.extend(f'{route}: duplicate id {key}' for key, count in Counter(page.ids).items() if count > 1)
        for reference in page.references:
            check_url(route, reference)
        for reference, label in page.links:
            target = urlsplit(urljoin(BASE + route, reference))
            label = label.strip().lower()
            if label == 'about' and target.path != urlsplit(BASE).path + 'about/':
                errors.append(f'{route}: About must open the dedicated page')
            if label == 'contact' or ('support' in label and not reference.startswith('#')) or 'contact the studio' in label or label == 'get in touch' or label == 'contact body hub':
                if target.path != urlsplit(BASE).path + 'support/':
                    errors.append(f'{route}: contact action must open the form: {label}')
            if target.path == urlsplit(BASE).path + 'support/':
                expected = next((name for name, title in (('bodyhub', 'body hub'), ('strata', 'strata'), ('nadir', 'nadir')) if title in label), None)
                if expected is None and label in ('contact', 'get in touch', 'contact the studio through the support form'):
                    expected = next((name for name in ('bodyhub', 'strata', 'nadir') if f'/{name}/' in '/' + route), None)
                if expected and target.query != f'product={expected}':
                    errors.append(f'{route}: wrong product context for {label}')

    for reference in re.findall(r'url\(["\']?([^"\')]+)', (ROOT / 'styles.css').read_text(encoding='utf-8')):
        check_url('styles.css', reference)

    assert (ROOT / 'bodyhub/foreground-health-demo.mp4').is_file(), 'Missing public review video'
    assert (ROOT / '.nojekyll').is_file(), 'Missing Pages configuration'
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(pages)} pages; {references} links, fragments and assets; contact routing and product context.')


if __name__ == '__main__':
    check()
