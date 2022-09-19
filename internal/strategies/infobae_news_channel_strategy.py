import time

from internal.domain.news import News
from internal.strategies.news_channel_strategy import NewsChannelStrategy


class InfobaeNewsChannelStrategy(NewsChannelStrategy):
    def __init__(self):
        super().__init__('Infobae', 'https://www.infobae.com', "/ultimas-noticias/")

    def _extract_latest_news_from_page(self, soup):
        news_list = []
        anchors = soup.find_all("a", class_="nd-feed-list-card")
        for anchor in anchors:
            url = self._base_url + anchor["href"]
            image = anchor.find("img", class_="feed-list-image")
            image_url = image["src"]
            h2 = anchor.find("h2", class_="nd-feed-list-card-headline-lean")
            title = h2.text

            news = News(title=title, image_url=image_url, channel=self._name, url=url, published_at=time.gmtime())
            news_list.append(news)

        return news_list
