import motor.motor_asyncio as motor
from discord.ext import commands

__all__: list[str] = ["User"]


class User(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db
