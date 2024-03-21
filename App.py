import os
import asyncio
import pymongo
from pyrogram import Client
from os import environ as env
from importlib import import_module

class Config():
    API_ID = int(env.get("API_ID", "26850449"))
    SELF_WORKERS = int(env.get("SELF_WORKERS", "4"))
    API_HASH = str(env.get("API_HASH", "72a730c380e68095a8549ad7341b0608"))
    BOT_TOKEN = str(env.get("BOT_TOKEN", "6486942911:AAFsg5NLnpHeosWQNcFz2NtvhtUF1y311Sw"))
    SUDOERS = list(map(int, env.get("SUDOERS", "6517565595 5896960462 5220416927").split()))
    MONGODB = str(env.get("MONGODB", "mongodb+srv://MrsMayura:Mayura6969@cluster0.5gpauan.mongodb.net/?retryWrites=true&w=majority"))

__version__ = ({"version": 0.1})
mongo = pymongo.MongoClient(Config.MONGODB)
usersdb = mongo["SoumoDB"]["users"]
groupdb = mongo["SoumoDB"]["group"]

def db_users():
    return len(list(usersdb.find({})))

def db_groups():
    return len(list(groupsdb.find({})))

def check_user(user):
    users = usersdb.find_one({"user_id" : int(user)})
    if not users:
        return False
    return True

def check_group(group):
    groups = groupdb.find_one({"chat_id" : int(group)})
    if not groups:
        return False
    return True

def add_user(user):
    checkdb = check_user(user)
    if checkdb:
        return
    return usersdb.insert_one({"user_id": int(user)})

def add_group(group):
    checkdb = check_group(group)
    if checkdb:
        return
    return groupdb.insert_one({"chat_id": int(group)})
    
class Pyro():
    Soumo = Client(
        name="Maybe:Soumo",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="Packages"),
        workers=Config.SELF_WORKERS,
        in_memory=True
    )
app = Pyro.Soumo

Loop = asyncio.get_event_loop()

async def addPackages():
    for mods in ALL_MODULES:
        import_module("Packages." + mods)
    print("» Dᴇᴘʟᴏʏ Sᴜᴄᴄᴇssғᴜʟʟʏ !")

if __name__ == "__main__":
    app.run()
    Loop.run_until_complete(addPackages())
