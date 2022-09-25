import http
import secrets

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from internal.configs.settings import Settings

security = HTTPBasic()


def validate_news_api_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    is_valid_username = secrets.compare_digest(Settings.get_api_username(), credentials.username)
    is_valid_password = secrets.compare_digest(Settings.get_api_password(), credentials.password)

    are_credentials_valid = is_valid_username and is_valid_password

    if not are_credentials_valid:
        raise HTTPException(status_code=http.HTTPStatus.UNAUTHORIZED, detail=http.HTTPStatus.UNAUTHORIZED.phrase)
