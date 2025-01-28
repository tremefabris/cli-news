from json import load as jload

from .color import Color as C
from .date import parse_date, format_date, date_ok



def extract_url(tag, html=True):
    if html:
        return tag.a["href"]
    return tag.link.text

def extract_title(tag, html=True):
    if html:
        return tag.text.strip()
    return tag.title.text.strip()

def extract_href(tag, html=True):
    url = extract_url(tag, html)
    title = extract_title(tag, html)
    return href(url, title)

def href(uri, label=None):
    if label is None:
        label = uri
    params = ''

    escape_mask = "\033]8;{};{}\033\\{}\033]8;;\033\\"
    return escape_mask.format(params, uri, label)



def format_output(href, news_source, formatted_date, color="blue"):
    
    return "[{}{}] {}".format(
        C.color(news_source, color=color),
        formatted_date,
        href
    )


def create_links(website, headlines, options):
    if website["date_format"] is None:
        print(f" :: {C.yellow('WARNING')} :: Publication date not available...")
        print(f" :: {C.yellow('WARNING')} :: Fetching all articles found...")

    links = []
    for h in headlines:

        h_date = parse_date(h, website["date_format"])
        if not date_ok(h_date, options.data):
            continue

        links.append(
            format_output(
                extract_href(h, website["html"]),
                options.jornal.upper(),
                format_date(h_date),
                options.hue
            )
        )

    return links


def get_website_config(website_path, options):
    with open(website_path.absolute(), "r") as f:
        ws = jload(f)
    news_source = options.jornal.lower()                            # error-passive -- why tho? lmao
    return ws[news_source]

def get_webheader_config(webheader_path, options=None):
    with open(webheader_path.absolute(), "r") as f:
        wh = jload(f)
    return wh

def get_website_and_header(website_path, webheader_path, options):
    ws = get_website_config(website_path, options)
    wh = get_webheader_config(webheader_path, options)
    return ws, wh


def filter_by_words(headlines, words, html=True):                   # all this badness just to preserve
    headlines_to_remove = []                                        # bs4 ResultSet's format...

    if words is not None:
        for h in headlines:
            word_match = False

            for w in words:
                if w.lower() in extract_title(h, html).lower():
                    word_match = True

            if not word_match:
                headlines_to_remove.append(h)
    
        for hrem in headlines_to_remove:
            headlines.remove(hrem)
