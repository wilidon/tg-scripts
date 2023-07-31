from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    TG_SESSION_NAME: str
    API_ID: int
    API_HASH: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
