from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    PyprojectTomlConfigSettingsSource,
    SettingsConfigDict,
)


class TelegramSettings(BaseSettings):
    auth_token: str
    group_id: str

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


telegram_settings = TelegramSettings()

print(f'{telegram_settings=}')