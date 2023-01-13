import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5615896308:AAFLUwNCx6DWgpj-MSPbKdOKFlyeokDL6B0")
    APP_ID = int(os.environ.get("APP_ID", 14699743))
    API_HASH = os.environ.get("API_HASH", "0cef89ed2c8025c16d2b4d42a1b8d792")
    USER_NAME = os.environ.get("USER_NAME", "Savior_128")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5059280908").split())
    BANNED_USER = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    OUO_IO_API_KEY = ""
    MAX_MESSAGE_LENGTH = 4096
    BOT_PWD = os.environ.get("BOT_PASSWORD", "123456")
    LOGGED_USER = []
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Saviororg:<password>@cluster0.tmqkdun.mongodb.net/?retryWrites=true&w=majority")
