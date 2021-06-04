import logging
from datetime import datetime

import discord
import motor.motor_asyncio as motor
import pymongo.errors as pymongo

from misc.config import DATABASE

CLIENT: motor.AsyncIOMotorClient = motor.AsyncIOMotorClient(DATABASE.address)


async def setup(db: motor.AsyncIOMotorDatabase) -> None:
    for collection in ["users", "bans", "kicks", "mutes", "warns", "censored"]:
        try:
            await db.create_collection(collection)
        except pymongo.CollectionInvalid:
            logging.warning(f"Collection already exists: {collection}")
            continue


async def add_entry(db: motor.AsyncIOMotorDatabase, collection: str, author: discord.Member, member: discord.Member,
                    reason: str) -> None:
    await add_user(db, member)
    await add_user(db, author)

    document: dict = {
        "member_id": member.id,
        "reason": reason,
        "reporter": author.id,
        "timestamp": datetime.now(),
    }
    db[collection].insert_one(document)


async def add_user(db: motor.AsyncIOMotorDatabase, member: discord.Member) -> None:
    if await db["users"].find_one({"_id": member.id}) is None:
        document: dict = {
            "_id": member.id,
            "name": f"{member.name}#{member.discriminator}",
        }
        await db["users"].insert_one(document)


async def add_word(db: motor.AsyncIOMotorDatabase, word: str) -> bool:
    try:
        await db["censored"].insert_one({"_id": word.lower()})
    except pymongo.DuplicateKeyError:
        return False
    return True


async def delete_word(db: motor.AsyncIOMotorDatabase, word: str) -> bool:
    if await db["censored"].find_one({"_id": word.lower()}):
        await db["censored"].delete_one({"_id": word.lower()})
        return True
    return False
