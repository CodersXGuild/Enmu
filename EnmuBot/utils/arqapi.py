import json
import sys
from random import randint
from time import time

import aiohttp
from EnmuBot import aiohttpsession 
from aiohttp import ClientSession

from google_trans_new import google_translator
from Python_ARQ import ARQ
from search_engine_parser import GoogleSearch

from EnmuBot import BOT_ID, OWNER_ID, ARQ_API_URL, ARQ_API_KEY
from EnmuBot import pbot

ARQ_API = "IRYCJR-TSZKHR-OHXCMD-IYJQQT-ARQ"
ARQ_API_KEY = "IRYCJR-TSZKHR-OHXCMD-IYJQQT-ARQ"
SUDOERS = OWNER_ID
ARQ_API_URL = "https://thearq.tech"

# Aiohttp Client
print("[INFO]: INITIALZING AIOHTTP SESSION")
aiohttpsession = ClientSession()
# ARQ Client
print("[INFO]: INITIALIZING ARQ CLIENT")
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

app = pbot
import socket
