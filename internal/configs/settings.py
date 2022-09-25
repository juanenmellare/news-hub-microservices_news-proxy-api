import os


class Settings:
    @staticmethod
    def get_api_username():
        return os.getenv("API_USERNAME", "admin")

    @staticmethod
    def get_api_password():
        return os.getenv("API_PASSWORD", "password")
