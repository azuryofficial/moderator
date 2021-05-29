import logging

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
