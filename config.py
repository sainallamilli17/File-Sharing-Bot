import os
import logging
from logging.handlers import RotatingFileHandler

BOT_TOKEN = "7543846429:AAF5GDFBCDsM_tghg6g3MXnZW_Ol5Xx5Occ"
API_ID = 979826
API_HASH = "238183386c30590d073b457166ba260d"

OWNER_ID = 1074804932
DB_URL = "mongodb+srv://ygovcu:fY1f9Wovol3NqhUX@cluster0.1mdno.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "madflixbotz"

CHANNEL_ID = -1001847420676
FORCE_SUB_CHANNEL = -1002358532189
FORCE_SUB_CHANNEL2 = 0
FORCE_SUB_CHANNEL3 = 0
FORCE_SUB_CHANNEL4 = 0

FILE_AUTO_DELETE = 600  # auto delete in seconds

PORT = "8080"
TG_BOT_WORKERS = 4

try:
    ADMINS = [6848088376]
    for x in (os.environ.get("ADMINS", "6848088376").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

CUSTOM_CAPTION = None
PROTECT_CONTENT = False
DISABLE_CHANNEL_BUTTON = True

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"
START_MSG = "Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link."
FORCE_MSG = "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(6848088376)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
