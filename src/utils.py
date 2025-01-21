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
    return tag.title.text

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
        if not date_ok(h_date, options.date):
            continue

        links.append(
            format_output(
                extract_href(h, website["html"]),
                options.jornal.upper(),
                format_date(h_date),
                options.color
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
