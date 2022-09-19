from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import news, channels

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(news.router)
app.include_router(channels.router)


@app.get("/")
def ping():
    return "news-proxy"


@app.get("/ping")
def ping():
    return "pong!"
