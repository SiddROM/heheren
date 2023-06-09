import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6129167866:AAGIEh5O1Zgt_9GLRc3pmaUq6VYeVvTca5o")

    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 25341724))
    API_HASH = os.environ.get("752a1fb86785c5bd35eb7b1e42071786")
    # Get these values from my.telegram.org

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5925926828 5860097723 1065732478 5895510545 6046532356").split())

    # Ban Unwanted Members..
    BANNED_USERS = []

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # Database url
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://jairename:jairename@cluster0.a1rlm9j.mongodb.net/?retryWrites=true&w=majority")

