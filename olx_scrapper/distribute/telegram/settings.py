from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class TelegramSettings(BaseSettings):
    auth_token: str
    chat_id: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


telegram_settings = TelegramSettings()

print(f"{telegram_settings=}")
