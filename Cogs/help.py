import motor.motor_asyncio as motor
from discord.ext import commands

from misc import HelpEmbed


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db

    @commands.command()
    async def help(self, ctx: commands.Context) -> None:
        await ctx.send(embed=HelpEmbed())
