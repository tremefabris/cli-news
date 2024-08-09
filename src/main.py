# TODO: Properly "deploy" program
# TODO: Add functionality to insert new websites (without hardcoding them)
# TODO: Type-hint everything
# TODO: Switch URL handling to urllib
# TODO: Make options.since better (allow strings as input, etc)
# TODO: Allow user to choose G1's RSS channel
# TODO: Proper logging

# G1 RSSs: https://g1.globo.com/tecnologia/noticia/2012/11/siga-o-g1-por-rss.html
# NEXO RSS: https://www.nexojornal.com.br/rss.xml


import requests
from bs4 import BeautifulSoup
from pathlib import Path

from .utils import create_links, get_website_and_header
from .options import get_options

def run():
    opt = get_options()
    WEBSITE, HEADER = get_website_and_header(Path("src/data/websites.json"),
                                             Path("src/data/webheaders.json"),
                                             opt)

    response = requests.get(WEBSITE["url"], headers=HEADER)

    if response.status_code == 200:
        parser = "html.parser" if WEBSITE["html"] else "xml"
        
        soup = BeautifulSoup(response.content, parser)
        headlines = soup.find_all(*WEBSITE["find_tag"])

        for link in create_links(WEBSITE, headlines, opt):
            print(link)
