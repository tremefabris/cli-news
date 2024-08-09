from datetime import datetime


def extract_date(tag, date_format):
    if date_format is None:
        return None
    return tag.pubDate.text

def parse_date(pub_date, date_format):

    if pub_date is None:
        date = None
    else:
        date = datetime.strptime(pub_date, date_format)
    
    return date

def format_date(tag, date_format):
    FINAL_FORMAT = " | %a, %d/%m/%Y"
    
    date = parse_date(
        extract_date(tag, date_format),
        date_format
    )

    if date is None:
        return ""
    return date.strftime(FINAL_FORMAT)
