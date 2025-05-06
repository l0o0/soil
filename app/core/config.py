import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ENV: str = "dev"
    SECRET_KEY: str
    ENCRYPT_ALGORITHM: str
    DATABASE_URI: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ECHO_SQL: bool = False

    model_config = SettingsConfigDict(
        env_file=f".env.{os.getenv("ENV", "dev") }",
        env_file_encoding="utf-8"
    )


settings = Settings()  # type: ignore
# print(f"Loading settings from {settings.model_dump_json()}")