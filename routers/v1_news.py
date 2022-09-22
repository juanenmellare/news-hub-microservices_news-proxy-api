import http

from fastapi import APIRouter, HTTPException, Depends

from internal.api.news_list_response import NewsListResponse
from internal.enums.news_channel import NewsChannel, get_news_channels_names
from internal.middlewares.validate_news_api_credentials import validate_news_api_credentials

router = APIRouter(prefix="/v1/news")


@router.get("/latest", dependencies=[Depends(validate_news_api_credentials)])
def get_latest(channels: str = None):
    news_channels_keys = get_news_channels_names()
    channel_names: []
    if channels:
        channel_names = channels.strip().upper().split(",")
        if not all(candidate in news_channels_keys for candidate in channel_names):
            raise HTTPException(status_code=http.HTTPStatus.BAD_REQUEST,
                                detail="'channels' query params should be any of these values [{}]"
                                .format(",".join(news_channels_keys)))
    else:
        channel_names = news_channels_keys

    channel_news_list = []
    for channel_name in channel_names:
        channel_news = NewsChannel[channel_name].value.get_latest_news()
        channel_news_list.extend(channel_news)

    return NewsListResponse(channel_news_list)
