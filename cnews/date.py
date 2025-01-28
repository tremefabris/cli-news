from datetime import datetime


def extract_date(tag, date_format):
    if date_format is None:
        return None
    return tag.pubDate.text

def parse_date(tag, date_format):

    pub_date = extract_date(tag, date_format)

    if pub_date is None:
        date = None
    else:
        date = datetime.strptime(pub_date, date_format)             # remove timezone info
    
    return date

def format_date(date):
    FINAL_FORMAT = " | %a, %d/%m/%Y"

    if date is None:
        return ""
    return date.strftime(FINAL_FORMAT)

def date_ok(date, days_since):
    if date is None or days_since < 0:
        return True

    TODAY = datetime.today()
    difference = TODAY.day - date.day

    return difference <= days_since
