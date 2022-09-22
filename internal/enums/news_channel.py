from enum import Enum
from internal.strategies.infobae_news_channel_strategy import InfobaeNewsChannelStrategy


class NewsChannel(Enum):
    INFOBAE = InfobaeNewsChannelStrategy()


def get_news_channels_names():
    names = []
    for channel in NewsChannel:
        names.append(channel.name)

    return names
