import logging

import discord
import motor.motor_asyncio as motor
import pymongo.errors as pymongo
from dotenv import dotenv_values

CLIENT: motor.AsyncIOMotorClient = motor.AsyncIOMotorClient(dotenv_values(".env")["DB"])


async def setup(db: motor.AsyncIOMotorDatabase) -> None:
    for collection in ["users", "bans", "kicks", "mutes", "warns"]:
        try:
            await db.create_collection(collection)
        except pymongo.CollectionInvalid:
            logging.error(f"Collection already exists: {collection}")
            continue


async def add_user(db: motor.AsyncIOMotorDatabase, member: discord.Member) -> None:
    document: dict = {
        "_id": member.id,
        "joined": member.joined_at,
        "messages": 0,
        "bans": 0,
        "kicks": 0,
        "mutes": 0,
        "warns": 0,
    }
    await db["users"].insert_one(document)
