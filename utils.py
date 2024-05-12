from json import load as jload

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

# TODO: Make this function better -- maybe create Color class
def format_output(href, news_source, _blue=True):
    if _blue:
        return "[\033[94m{}\033[0m] {}".format(
            news_source,
            href
        )


def create_links(website, headlines, options):
    links = []
    for h in headlines:
        links.append(
            format_output(
                extract_href(h, website["html"]),
                options.jornal.upper()
            )
        )
    return links


def get_website_config(website_path, options):
    with open(website_path, "r") as f:
        ws = jload(f)
    src = options.jornal.lower()  # error-passive
    return ws[src]

def get_webheader_config(webhead_path, options=None):
    with open(webhead_path, "r") as f:
        wh = jload(f)
    return wh

def get_website_and_header(website_path, webheader_path, options):
    ws = get_website_config(website_path, options)
    wh = get_webheader_config(webheader_path, options)
    return ws, wh