# News Hub (microservices version) - News Proxy API

A simple API for use as a proxy for Argentine news channels.
<hr /> 

## Requirements
- Python 3.x
- pip
<hr /> 

## Setup _(Suggested)_
- Install `python` from https://www.python.org/downloads/.
- Clone this repository and move into the folder.
- Run ``pip install -r requirements.txt``.

<hr /> 

## Run Application
Start running the app locally with the following command ``uvicorn main:app --reload``.
If the application setup is ok you should see the following message and the application listening on `8000` port.
```console
news-hub-microservices_news-collector-api $uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['/Users/juanen/tesina/news-hub-microservices_news-collector-api']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [14786] using WatchFiles
INFO:     Started server process [14788]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
<hr /> 

## Run Tests

Run all tests, with the following command:
```console
pytest
```

Run all tests with code coverage + report, with the following command:
```console
coverage run -m pytest && coverage html && open htmlcov/index.html
```
