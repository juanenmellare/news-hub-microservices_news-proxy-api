import os


class Settings:
    @staticmethod
    def get_news_api_username():
        return os.getenv("NEWS_API_USERNAME", "admin")

    @staticmethod
    def get_news_api_password():
        return os.getenv("NEWS_API_PASSWORD", "password")
