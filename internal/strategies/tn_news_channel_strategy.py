from internal.domain.news import News
from internal.strategies.news_channel_strategy import NewsChannelStrategy
from internal.utils.web_scrapping_util import get_and_parse_html_soup


class TNNewsChannelStrategy(NewsChannelStrategy):
    def __init__(self):
        super().__init__('TN', 'https://tn.com.ar', '/ultimas-noticias/')

    def _extract_latest_news_from_page(self, soup):
        news_list = []
        articles = soup.find_all("article", class_="card__container card__horizontal")
        for article in articles:
            image = article.find("img", "image image_placeholder")
            image_url = image["src"]

            h2 = article.find("h2", class_="card__headline")
            anchor = h2.find("a")
            title = anchor.text
            url = self._base_url + anchor["href"]

            article_page = get_and_parse_html_soup(url)
            time = article_page.find("time", "time__container")
            published_at = time["datetime"]

            news = News(title=title, image_url=image_url, channel=self._name, url=url, published_at=published_at)
            news_list.append(news)

        return news_list
