from Graph.WebScrap import *

"mongodb+srv://nandhaxd:rw5T7YJRjsE3fmk3@cluster0.80igexg.mongodb.net/?retryWrites=true&w=majority"


MONGO_URI = ("mongodb+srv://MrsMayura:Mayura6969@cluster0.5gpauan.mongodb.net/?retryWrites=true&w=majority")
MOTOR_URI = ("mongodb+srv://RiasGremory:Rias6969@cluster0.37ripjq.mongodb.net/?retryWrites=true&w=majority")
from os import execvp
#from Linux import LOGGER
from sys import executable
from pymongo import MongoClient
from pyrogram.types import Message
from pymongo.errors import InvalidURI
from pymongo.errors import PyMongoError
from motor.motor_asyncio import AsyncIOMotorClient as MongoDB

try:
    db = MongoDB(MOTOR_URI)
except InvalidURI:
    pass #LOGGER.info("» Iɴᴠᴀʟɪᴅ ᴍᴏɴɢᴏ ᴜʀɪ ᴏʀ ɪᴛs ᴇxᴘɪʀᴇᴅ !")
except Exception as eos:
    pass #LOGGER.info(f"» Mᴏɴɢᴏ ᴍᴏᴛᴏʀ ᴄʟɪᴇɴᴛ ᴇʀʀᴏʀ : {eos}")
except PyMongoError:
    pass

try:
    mongo = MongoClient(MONGO_URI)
except InvalidURI:
    pass #LOGGER.info("» Iɴᴠᴀʟɪᴅ ᴍᴏɴɢᴏ ᴜʀɪ ᴏʀ ɪᴛs ᴇxᴘɪʀᴇᴅ !")
except Exception as eoc:
    pass #LOGGER.info(f"» Mᴏɴɢᴏ ᴄʟɪᴇɴᴛ ᴇʀʀᴏʀ : {eoc}")
except PyMongoError:
   pass

Rose = db["Soumo"]["Rose"]
usersdb = mongo["SoumoDB"]["users"]
groupdb = mongo["SoumoDB"]["group"]

async def Escove(Chat:int, Message:int) -> None:
    await Rose.update_one({"Soumo": "Soumo"}, {"$set": {"chat_id": Chat, "message_id": Message}}, upsert=True)

async def Clean_Stage() -> dict:
    Data = await Rose.find_one({"Soumo": "Soumo"})
    if not Data:
        return {}
    await Rose.delete_one({"Soumo": "Soumo"})
    return {"chat_id": Data["chat_id"], "message_id": Data["message_id"]}

async def Restart(msg:Message) -> None:
    if msg:
        await Escove(msg.chat.id, msg.id)
    execvp(executable, [executable, "-m", "Linux"])

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
