import requests
from bs4 import BeautifulSoup


def get_and_parse_html_soup(url):
    page_response = requests.get(url)

    return BeautifulSoup(page_response.content, "html.parser")
