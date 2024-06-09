from os import environ as env
from os import getenv

API_ID = int(env.get("API_ID", "26850449"))
SUPPORT = int(env.get("SUPPORT", "-1001535967539"))
PREFIXS = list(env.get("PREFIXS", "? * $ . ! /").split())
API_HASH = str(env.get("API_HASH", "72a730c380e68095a8549ad7341b0608"))
BOT_TOKEN = str(env.get("BOT_TOKEN", "6486942911:AAFsg5NLnpHeosWQNcFz2NtvhtUF1y311Sw"))
SUDOERS = list(map(int, env.get("SUDOERS", "6505111743 6517565595 5896960462 5220416927").split()))
GIST_IMAGE = str(env.get("GIST_IMAGE", "https://graph.org/file/5cb4b1a7faec81476f99c.jpg"))
GUARDS = list(map(int, env.get("GUARDS", " ").split()))

OWNER = int(getenv("OWNER", "6517565595"))
SUDOS = list(map(int, getenv("SUDOS", "6517565595").split()))
