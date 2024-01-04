import asyncio
import sys
from motor import motor_asyncio
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from EnmuBot.confing import get_int_key, get_str_key
from EnmuBot import LOGGER

client = MongoClient("mongodb+srv://enmu:enmu123@enmu.2cuev.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
client = MongoClient("mongodb+srv://enmu:enmu123@enmu.2cuev.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", 27017)["EnmuBot"]
motor = motor_asyncio.AsyncIOMotorClient("mongodb+srv://enmu:enmu123@enmu.2cuev.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", 27017)
db = motor["EnmuBot"]
db = client["EnmuBot"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(LOGGER.critical("ERROR"))
