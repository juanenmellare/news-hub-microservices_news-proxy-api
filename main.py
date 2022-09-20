from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import v1_news, v1_channels

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(v1_news.router)
app.include_router(v1_channels.router)


@app.get("/")
def ping():
    return "news-proxy"


@app.get("/ping")
def ping():
    return "pong!"
