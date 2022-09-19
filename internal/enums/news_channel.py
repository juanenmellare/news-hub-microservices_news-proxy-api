from enum import Enum
from internal.strategies.infobae_news_channel_strategy import InfobaeNewsChannelStrategy


class NewsChannel(Enum):
    INFOBAE = InfobaeNewsChannelStrategy()


def get_news_channels_keys():
    keys = []
    for channel in NewsChannel:
        keys.append(channel.name)
    return keys
