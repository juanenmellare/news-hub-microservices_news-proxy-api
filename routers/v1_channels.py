import http

from fastapi import APIRouter, HTTPException, Depends

from internal.domain.news_list import NewsList
from internal.enums.news_channel import NewsChannel, get_news_channels_keys
from internal.middlewares.validate_news_api_credentials import validate_news_api_credentials

router = APIRouter(prefix="/v1/channels")


@router.get("/{channel}/latest", dependencies=[Depends(validate_news_api_credentials)])
def get_latest_by_channel(channel: str):
    news_channels_keys = get_news_channels_keys()
    channel_formatted = channel.upper()
    if channel_formatted not in news_channels_keys:
        raise HTTPException(status_code=http.HTTPStatus.BAD_REQUEST,
                            detail="'{}' is not a valid 'channel', should be any of these values [{}]"
                            .format(channel, ",".join(news_channels_keys)))

    channel_news_list = NewsChannel[channel_formatted].value.get_latest_news()

    return NewsList(channel_news_list)
