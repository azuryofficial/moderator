import logging
from datetime import datetime

import discord
import motor.motor_asyncio as motor
import pymongo.errors as pymongo

from misc.config import DATABASE, COMMANDS

__all__: list[str] = ["CLIENT", "setup", "add_entry", "add_user", "add_word", "delete_word"]

CLIENT: motor.AsyncIOMotorClient = motor.AsyncIOMotorClient(DATABASE.address)


async def setup(db: motor.AsyncIOMotorDatabase) -> None:
    collections: list[str] = [COMMANDS[command].collection for command in COMMANDS]
    for collection in collections:
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
    if await db[COMMANDS["USER"].collection].find_one({"_id": member.id}) is None:
        document: dict = {
            "_id": member.id,
            "name": f"{member.name}#{member.discriminator}",
        }
        await db[COMMANDS["USER"].collection].insert_one(document)


async def add_word(db: motor.AsyncIOMotorDatabase, word: str) -> bool:
    try:
        await db[COMMANDS["CENSOR"].collection].insert_one({"_id": word.lower()})
    except pymongo.DuplicateKeyError:
        return False
    return True


async def delete_word(db: motor.AsyncIOMotorDatabase, word: str) -> bool:
    if await db[COMMANDS["CENSOR"].collection].find_one({"_id": word.lower()}):
        await db[COMMANDS["CENSOR"].collection].delete_one({"_id": word.lower()})
        return True
    return False
