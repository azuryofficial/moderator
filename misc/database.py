import logging

import discord
import motor.motor_asyncio as motor
import pymongo.errors as pymongo
from discord.ext import commands
from dotenv import dotenv_values

from Cogs.user import User

CLIENT: motor.AsyncIOMotorClient = motor.AsyncIOMotorClient(dotenv_values(".env")["DB"])


async def setup(db: motor.AsyncIOMotorDatabase) -> None:
    for collection in ["users", "bans", "kicks", "mutes", "warns"]:
        try:
            await db.create_collection(collection)
        except pymongo.CollectionInvalid:
            logging.error(f"Collection already exists: {collection}")
            continue


async def add_entry(db: motor.AsyncIOMotorDatabase, collection: str, ctx: commands.Context, member: discord.Member,
                    reason: str) -> None:
    await User.add_user(db, member)
    await User.add_user(db, ctx.message.author.id)

    document: dict = {
        "member_id": member.id,
        "reason": reason,
        "reporter": ctx.message.author.id,
        "timestamp": ctx.message.created_at,
    }
    db[collection].insert_one(document)


async def add_user(db: motor.AsyncIOMotorDatabase, member: discord.Member) -> None:
    if await db["users"].find_one({"_id": member.id}) is None:
        await db["users"].insert_one({"_id": member.id})
