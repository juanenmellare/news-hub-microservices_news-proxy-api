import requests

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class NewsChannelStrategy(ABC):
    def __init__(self, name, base_url, latest_news_url):
        self._name = name
        self._base_url = base_url
        self._latest_news_url = latest_news_url

    def __get_latest_news_html(self):
        return requests.get(self._base_url + self._latest_news_url)

    @abstractmethod
    def _extract_latest_news_from_page(self, soup):
        pass

    def get_latest_news(self):
        page_response = self.__get_latest_news_html()
        soup = BeautifulSoup(page_response.content, "html.parser")
        news = self._extract_latest_news_from_page(soup)

        return news
