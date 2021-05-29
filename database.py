import logging

import motor.motor_asyncio as motor
import pymongo.errors as pymongo
from dotenv import dotenv_values

CLIENT: motor.AsyncIOMotorClient = motor.AsyncIOMotorClient(dotenv_values(".env")["DB"])


async def setup(db: motor.AsyncIOMotorDatabase, collections: list[str]) -> None:
    for collection in collections:
        try:
            await db.create_collection(collection)
        except pymongo.CollectionInvalid:
            logging.error(f"Collection already exists: {collection}")
            continue
