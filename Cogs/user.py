import discord
import motor.motor_asyncio as motor
from discord.ext import commands


class User(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @staticmethod
    async def _add_user(db: motor.AsyncIOMotorCollection, member: discord.Member) -> None:
        if not await db["users"].find_one({"_id": member.id}):
            user_document: dict = {
                "_id": member.id,
                "joined_at": member.joined_at,
            }
            await db["users"].insert_one(user_document)
