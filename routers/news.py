from fastapi import APIRouter, HTTPException
from internal.enums.news_channel import NewsChannel, get_news_channels_keys

router = APIRouter(prefix="/news")


@router.get("/latest")
def get_latest(channels: str = None):
    news_channels_keys = get_news_channels_keys()
    channel_names: []
    if channels:
        channel_names = channels.strip().upper().split(",")
        if not all(candidate in news_channels_keys for candidate in channel_names):
            raise HTTPException(status_code=400,
                                detail="'channels' query params should be any of these values [{}]"
                                .format(",".join(news_channels_keys)))
    else:
        channel_names = news_channels_keys

    news_list = []
    for channel_name in channel_names:
        channel_news = NewsChannel[channel_name].value.get_latest_news()
        news_list.extend(channel_news)

    return news_list
