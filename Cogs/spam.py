import discord
from typing import Optional
import motor.motor_asyncio as motor
from discord.ext import commands

__all__: list[str] = ["Spam"]


class Spam(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return None

        last_message: Optional[discord.Message] = None
        async for last in message.channel.history(limit=1, before=message):
            last_message = last

        if (
                last_message is not None and
                last_message.author == message.author and
                last_message.clean_content == message.clean_content and
                (message.created_at - last_message.created_at).total_seconds() <= 2
        ):
            await message.delete()
