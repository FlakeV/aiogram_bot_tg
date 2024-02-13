import os
import dotenv
from logging import INFO

dotenv.load_dotenv(".env")


class AppConfig:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        AppConfig.__instance = None

    def __init__(self):
        self.bot_token = os.getenv("BOT_TOKEN")
        # self.admins = list(map(int, os.getenv("ADMINS").split(",")))
        self.log_level = INFO
        self.chanel_id = int(os.getenv("CHANEL_ID"))

        self.db_url = f'postgresql+asyncpg://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'


app_config = AppConfig()
