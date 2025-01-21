# TODO: Properly "deploy" program
# TODO: Add functionality to insert new websites (without hardcoding them)
# TODO: Type-hint everything
# TODO: Switch URL handling to urllib
# TODO: Make options.since better (allow strings as input, etc)
# TODO: Modularize RSS checking; each time, break down on '/'
# TODO: Allow user to choose where to log
# TODO: Add argument parsing in bash

# G1 RSSs: https://g1.globo.com/tecnologia/noticia/2012/11/siga-o-g1-por-rss.html
# NEXO RSS: https://www.nexojornal.com.br/rss.xml


from pathlib import Path

from .options import get_options
from .utils import create_links, get_website_and_header
from .net import get_headlines_from_website
from .color import Color as C
from .log import Log


def run():
    opt = get_options()
    WEBSITE, HEADER = get_website_and_header(Path("src/data/websites.json"),
                                             Path("src/data/webheaders.json"),
                                             opt)
    
    if not WEBSITE["has_channels"] and opt.canal is not None:
        Log("This `jornal` does not have different RSS channels",
            "Using main RSS channel available",
            level = Log.WARNING)
        opt.canal = None

    url = WEBSITE["url"] + opt.canal if opt.canal is not None else WEBSITE["url"]
    parser = "html.parser" if WEBSITE["html"] else "xml"
    find_tag = WEBSITE["find_tag"]

    headlines = get_headlines_from_website(url, parser, find_tag, HEADER)

    if len(headlines) == 0:
        Log("RSS channel is empty",
            "Defaulting to main RSS channel",
            level = Log.WARNING)
        headlines = get_headlines_from_website(WEBSITE["url"], parser, find_tag, HEADER)

        if len(headlines) == 0:
            Log("Main RSS channel unavailable",
                "Aborting execution",
                level = Log.ERROR)

    for link in create_links(WEBSITE, headlines, opt):
        print(link)
