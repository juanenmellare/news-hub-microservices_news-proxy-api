from enum import Enum
from internal.strategies.infobae_news_channel_strategy import InfobaeNewsChannelStrategy
from internal.strategies.tn_news_channel_strategy import TNNewsChannelStrategy


class NewsChannel(Enum):
    INFOBAE = InfobaeNewsChannelStrategy()
    TN = TNNewsChannelStrategy()


def get_news_channels_names():
    names = []
    for channel in NewsChannel:
        names.append(channel.name)

    return names
