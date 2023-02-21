from abc import ABC, abstractmethod

from internal.utils.web_scrapping_util import get_and_parse_html_soup


class NewsChannelStrategy(ABC):
    def __init__(self, name, base_url, latest_news_url):
        self._name = name
        self._base_url = base_url
        self._latest_news_url = latest_news_url

    def __get_latest_news_url(self):
        return self._base_url + self._latest_news_url

    @abstractmethod
    def _extract_latest_news_from_page(self, soup):
        pass

    def get_latest_news(self):
        latest_new_url = self.__get_latest_news_url()
        soup = get_and_parse_html_soup(latest_new_url)
        news = self._extract_latest_news_from_page(soup)

        return news
