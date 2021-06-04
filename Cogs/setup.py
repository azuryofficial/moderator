import motor.motor_asyncio as motor
from discord.ext import commands

from misc import setup

__all__: list[str] = ["Setup"]


class Setup(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db

    @commands.Cog.listener()
    async def on_connect(self) -> None:
        await setup(self.db)
