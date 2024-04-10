import argparse
import requests
from bs4 import BeautifulSoup

def href(uri, label=None):
    # https://stackoverflow.com/questions/40419276/python-how-to-print-text-to-console-as-hyperlink
    if label is None:
        label = uri
    params = ''

    escape_mask = "\033]8;{};{}\033\\{}\033]8;;\033\\"
    return escape_mask.format(params, uri, label)

# TODO: Make this function better -- maybe create Color class
def format_output(href, news_source, _blue=True):
    if _blue:
        return "[\033[94m{}\033[0m] {}".format(
            news_source,
            href
        )


def extract_url(tag, html=True):
    if html:
        return tag.a["href"]
    return tag.link.text
def extract_title(tag, html=True):
    if html:
        return tag.text.strip()
    return tag.title.text
def extract_href(tag, html=True):
    url = extract_url(tag, html)
    title = extract_title(tag, html)
    return href(url, title)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--jornal", "-j", type=str, required=True)

    return parser.parse_args()

opt = get_args()

# G1 RSSs: https://g1.globo.com/tecnologia/noticia/2012/11/siga-o-g1-por-rss.html

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

WEBSITES = {
    "JAV": {
        "url": "https://averdade.org.br/",
        "html": True,
        "find_tag": ("h3", {"class":"entry-title td-module-title"}),
    },
    "g1": {
        "url": "https://g1.globo.com/rss/g1/",
        "html": False,
        "find_tag": ("item",)
    },
    "NEXO": {
        "url": "https://www.nexojornal.com.br/rss.xml",
        "html": False,
        "find_tag": ("item",)
    },
}

SOURCE = opt.jornal
SITE = WEBSITES[SOURCE]

response = requests.get(SITE["url"], headers=HEADERS)

if response.status_code == 200:
    parser = "html.parser" if SITE["html"] else "xml"
    
    soup = BeautifulSoup(response.content, parser)
    headlines = soup.find_all(*SITE["find_tag"])

    for h in headlines:

        article_href = extract_href(h, SITE["html"])
        output = format_output(article_href, SOURCE)

        print(output)
