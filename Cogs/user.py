import discord
import motor.motor_asyncio as motor
from discord.ext import commands


class User(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db

    async def add_user(self, db: motor.AsyncIOMotorDatabase, member: discord.Member) -> None:
        if not await self.user_exists(db, member):
            user_document: dict = {"_id": member.id}
            await db["users"].insert_one(user_document)

    @staticmethod
    async def user_exists(db: motor.AsyncIOMotorDatabase, member: discord.Member) -> bool:
        return await db["users"].find_one({"_id": member.id}) is not None
