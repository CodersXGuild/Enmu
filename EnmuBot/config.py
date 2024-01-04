import json
import os


def get_user_list(config, key):
    with open("{}/EnmuBot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True
    TEMP_DOWNLOAD_DIRECTORY = "/tmp"
    API_ID = 17807190  
    API_HASH = "87d7db377d986df687a32d8230314e7f"
    ARQ_API = "RVLOWH-KMDHXW-QQCPAC-EFICND-ARQ"
    TOKEN = "5107955346:AAHR9He_np6W8XdcNMgOjfkCXEJJ8_XqxZg"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    BOT_ID = 5222559003
    OWNER_ID = 2005266280  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Lost_Emotion"
    SUPPORT_CHAT = "Enmu_chat_Support"  # Your own group for support, do not add the @
    BOT_USERNAME = "Enmu_KIZUKI_BOT"
    JOIN_LOGGER = (
        -1001774850421
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001774850421
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    ERROR_LOGS = (
        -1001711427851
    )  # Prints information Error
    REDIS_URL = "redis://default:cdgiOMJGyZsqx97p5S7S@containers-us-west-27.railway.app:6644"
    MONGO_DB_URI = "mongodb+srv://enmu:enmu123@enmu.2cuev.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = "postgresql://postgres:nR1yc3HQjFJSJcXBy4V3@containers-us-west-33.railway.app:7793/railway"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "-0X68BOFAQTLJ"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "6950f559377140a4e1594c564cdca6a3"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    REM_BG_API_KEY = "-QcoQXCAXyhAxeLN2eD86LeFa"
    OPENWEATHERMAP_ID = "887da2c60d9f13fe78b0f9d0c5cbaade"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
