import asyncio
import logging
import os
import sys
import json
import asyncio
import time
import telegram.ext as tg
from EnmuBot.services.quoteapi import Quotly

from Python_ARQ import ARQ
from redis import StrictRedis
from inspect import getfullargspec
from aiohttp import ClientSession
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.sessions import MemorySession
from pyrogram.types import Message
from pyrogram import Client, errors
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, ChannelInvalid
from pyrogram.types import Chat, User
from ptbcontrib.postgres_persistence import PostgresPersistence

StartTime = time.time()
quotly = Quotly()

def get_user_list(__init__, key):
    with open("{}/EnmuBot/{}".format(os.getcwd(), __init__), "r") as json_file:
        return json.load(json_file)[key]

    
    
    
    



# enable logging
FORMAT = "[EnmuBot] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger('ptbcontrib.postgres_persistence.postgrespersistence').setLevel(logging.WARNING)

LOGGER = logging.getLogger('[EnmuBot]')
LOGGER.info("Enmu is starting. | A Project by t.me/TITANHEADQUATERS | Licensed under GPLv3.")
LOGGER.info("Hehe Baka I know I died but I died in a cool way.")
LOGGER.info("Project maintained by: github.com/CodersXGuild (t.me/Rickx_2005)")

# if version < 3.9, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 9:
    LOGGER.error(
        "Baka You MUST have a python version of at least 3.9! Multiple features depend on this. Enmu quitting."
    )
    sys.exit(1)



TOKEN = ""

try:
        OWNER_ID = 
except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

JOIN_LOGGER = ( )
OWNER_USERNAME = 
try:
        DRAGONS = []
        DEV_USERS = []
except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

try:
        DEMONS = []
except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

try:
        WOLVES = []
except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

try:
        TIGERS = []
except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

EVENT_LOGS = ( )
WEBHOOK = False
URL = None
PORT = 5000
CERT_PATH = None
REDIS_URL = ""
API_ID = 
API_HASH = ""
ERROR_LOGS = ( )
MONGO_DB_URI = ""
DONATION_LINK = "I'm Free for everyone"
LOAD = []
TEMP_DOWNLOAD_DIRECTORY = "/tmp"
NO_LOAD = []
DEL_CMDS = True
ARQ_API_KEY = ""
ARQ_API_URL = "https://arq.hamker.in"
STRICT_GBAN = True
WORKERS = (8)
REM_BG_API_KEY = ("")
BAN_STICKER = ""
ALLOW_EXCL = True
WALL_API = ("")
SUPPORT_CHAT = ""
INFOPIC = True
BOT_USERNAME = ""
BOT_ID = 
OK = []

try:
        BL_CHATS = {int(x) for x in OK or []}
except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")

REDIS = StrictRedis.from_url(REDIS_URL,decode_responses=True)

try:

    REDIS.ping()

    LOGGER.info("Your redis server is now alive!")

except BaseException:

    raise Exception("Your redis server is not alive, please check again.")

finally:

   REDIS.ping()

   LOGGER.info("Your redis server is now alive!")
    
    
from EnmuBot.modules.sql import SESSION

defaults = tg.Defaults(run_async=True)
updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient(MemorySession(), API_ID, API_HASH)
dispatcher = updater.dispatcher
print("[INFO]: INITIALIZING AIOHTTP SESSION")
aiohttpsession = ClientSession()
# ARQ Client
print("[INFO]: INITIALIZING ARQ CLIENT")
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

session_name = TOKEN.split(":")[0]
pbot = Client(session_name, api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
Riz = TelegramClient('Bamall', API_ID, API_HASH).start(bot_token=TOKEN)
LOGGER.info("Your BamAll is now Started!!!")

apps = []
apps.append(pbot)
loop = asyncio.get_event_loop()

async def get_entity(client, entity):
    entity_client = client
    if not isinstance(entity, Chat):
        try:
            entity = int(entity)
        except ValueError:
            pass
        except TypeError:
            entity = entity.id
        try:
            entity = await client.get_chat(entity)
        except (PeerIdInvalid, ChannelInvalid):
            for kp in apps:
                if kp != client:
                    try:
                        entity = await kp.get_chat(entity)
                    except (PeerIdInvalid, ChannelInvalid):
                        pass
                    else:
                        entity_client = kp
                        break
            else:
                entity = await kp.get_chat(entity)
                entity_client = kp
    return entity, entity_client


async def eor(msg: Message, **kwargs):
    func = msg.edit_text if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})


DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)

# Load at end to ensure all prev variables have been set
from EnmuBot.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler
