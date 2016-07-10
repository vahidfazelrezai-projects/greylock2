from bs4 import BeautifulSoup
from htmlmin.minify import html_minify

def simplify(html):
    soup = BeautifulSoup(html, 'html.parser')
    [s.extract() for s in soup('script')]
    [s.extract() for s in soup('link')]
    [s.extract() for s in soup('img')]

    soup.head.append(soup.new_tag("link", rel="stylesheet", type="text/css", href="/static/style.css"))
    soup.head.append(soup.new_tag("script", src="/static/custom.js"))

    minhtml = html_minify(str(soup))
    return minhtml
