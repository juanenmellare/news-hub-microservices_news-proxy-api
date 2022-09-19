from enum import Enum
from internal.strategies.infobae_channel_strategy import InfobaeChannelStrategy


class NewsChannel(Enum):
    INFOBAE = InfobaeChannelStrategy()


def get_news_channels_keys():
    keys = []
    for channel in NewsChannel:
        keys.append(channel.name)
    return keys
