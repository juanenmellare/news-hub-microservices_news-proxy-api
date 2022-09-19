import http
from fastapi.testclient import TestClient

from internal.enums.news_channel import NewsChannel
from main import app

client = TestClient(app)


def get_default_news_channel_name():
    return NewsChannel.INFOBAE.name


def assert_equals(value, expected):
    assert value == expected


def assert_key_exist(value):
    assert value is not True


def test_root_route():
    response = client.get('/')

    assert response.status_code == http.HTTPStatus.OK
    assert response.text == '"news-proxy"'


def test_ping_route():
    response = client.get('/ping')

    assert response.status_code == http.HTTPStatus.OK
    assert response.text == '"pong!"'


def test_news_route_latest():
    response = client.get('/news/latest')

    assert_equals(response.status_code, http.HTTPStatus.OK)
    first_news = response.json()[0]
    assert_equals(len(first_news), 5)
    assert_equals(first_news['channel'], 'Infobae')
    assert_key_exist(first_news['image_url'])
    assert_key_exist(first_news['url'])
    assert_key_exist(first_news['title'])
    assert_key_exist(first_news['published_at'])


def test_news_route_latest_query_param_channels():
    response = client.get('/news/latest?channels={}'.format(get_default_news_channel_name()))

    assert_equals(response.status_code, http.HTTPStatus.OK)
    first_news = response.json()[0]
    assert_equals(len(first_news), 5)
    assert_equals(first_news['channel'], 'Infobae')
    assert_key_exist(first_news['image_url'])
    assert_key_exist(first_news['url'])
    assert_key_exist(first_news['title'])
    assert_key_exist(first_news['published_at'])


def test_news_route_latest_query_param_channels_bad_request():
    response = client.get('/news/latest?channels=foo')

    assert_equals(response.status_code, http.HTTPStatus.BAD_REQUEST)
    assert_equals(response.text, '{\"detail\":\"\'channels\' query params should be any of these values [INFOBAE]\"}')


def test_channel_route_channel_param_news():
    response = client.get('/channels/{}/latest'.format(get_default_news_channel_name()))

    assert_equals(response.status_code, http.HTTPStatus.OK)
    first_news = response.json()[0]
    assert_equals(len(first_news), 5)
    assert_equals(first_news['channel'], 'Infobae')
    assert_key_exist(first_news['image_url'])
    assert_key_exist(first_news['url'])
    assert_key_exist(first_news['title'])
    assert_key_exist(first_news['published_at'])


def test_channel_route_channel_param_news_bad_request():
    response = client.get('/channels/foo/latest')

    assert_equals(response.status_code, http.HTTPStatus.BAD_REQUEST)
    assert_equals(response.text, '{\"detail\":\"\'foo\' is not a valid \'channel\', should be any of these values [INFOBAE]\"}')
