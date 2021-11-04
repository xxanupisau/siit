import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "𝗚8𝗔𝗭𝗔𝗟 𝗠𝗨𝗦𝗜𝗖 🧞🎧⚡")
BG_IMAGE = getenv("BG_IMAGE", "https://i.imgur.com/6DGNhHU.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://i.imgur.com/6DGNhHU.jpg")
AUD_IMG = getenv("AUD_IMG", "https://i.imgur.com/6DGNhHU.jpg")
QUE_IMG = getenv("QUE_IMG", "https://i.imgur.com/6DGNhHU.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "XTafa_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "G8AZAAL")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Ghazal_Source")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Ghazal_Source")
OWNER_NAME = getenv("OWNER_NAME", "G8AZAAL") 
DEV_NAME = getenv("DEV_NAME", "G8AZAAL")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
