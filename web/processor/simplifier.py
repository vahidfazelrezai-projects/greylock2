from bs4 import BeautifulSoup
from htmlmin.minify import html_minify

def simplify(html):
    soup = BeautifulSoup(html, 'html.parser')
    minhtml = html_minify(str(soup))
    return minhtml
