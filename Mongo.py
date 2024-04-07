import os
import Config
from motor.motor_asyncio import AsyncIOMotorClient

MONGO = str(os.getenv("MONGO", "mongodb+srv://imtiazurrehman1122:HAs207933@cluster0.wxy7hze.mongodb.net/?retryWrites=true&w=majority"))
Mongo = AsyncIOMotorClient(MONGO)

userdb = Mongo["Gram"]["user"]

async def add_user(user_id: int, user_name: str):
    checkdb = await check_user(user_id)
    if checkdb:
        return
    return await userdb.insert_one(
        {
            "user_id": user_id,
            "user_name": user_name,
            "coins": 2500,
            "gems": 100,
            "manna": 15,
            "referral": 0,
            "referral_reward": 0,
            "invited": None
        }
    )

async def check_user(user_id: int):
    users = await userdb.find_one({"user_id" : user_id})
    if not users:
        return False
    return True

async def remove_user(user_id: int):
    users = await userdb.find_one({"user_id": user_id})
    if users:
        return await userdb.delete_one({"user_id": user_id})

async def user_data(user_id: int):
    user = await userdb.find_one({"user_id" : user_id})
    if not user:
        return
    return user
