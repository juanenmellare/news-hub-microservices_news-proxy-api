from fastapi import APIRouter, HTTPException
from internal.enums.news_channel import NewsChannel, get_news_channels_keys

router = APIRouter(prefix="/channels")


@router.get("/{channel}/latest")
def get_latest_by_channel(channel: str):
    news_channels_keys = get_news_channels_keys()
    channel_formatted = channel.upper()
    if channel_formatted not in news_channels_keys:
        raise HTTPException(status_code=400,
                            detail="'{}' is not a valid 'channel', should be any of these values [{}]"
                            .format(channel, ",".join(news_channels_keys)))

    channel_news = NewsChannel[channel_formatted].value.get_latest_news()

    return channel_news
