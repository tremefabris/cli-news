import requests
from bs4 import BeautifulSoup

from .color import Color as C


def get_headlines_from_website(url, parser, find_tag, header):

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, parser)
        headlines = soup.find_all(*find_tag)

        return headlines

