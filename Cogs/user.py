from collections import defaultdict
from datetime import datetime

import discord
import motor.motor_asyncio as motor
from discord.ext import commands

from misc import UserEmbed
from misc.config import COMMANDS

__all__: list[str] = ["User"]


class User(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db

    @commands.command(aliases=["userinfo", "uinfo", "userlog", "ulog"])
    async def user_info(self, ctx: commands.Context, member: discord.Member = None) -> None:
        if not member:
            member: discord.Member = ctx.author

        info: defaultdict = defaultdict(str)
        for amount in ["BAN", "KICK", "WARN", "MUTE"]:
            info[f"{amount.lower()}s"] = str(
                await self.db[COMMANDS[amount].collection].count_documents({"member_id": member.id}),
            )

        joined: datetime = datetime.strftime(member.joined_at, COMMANDS["USER"].format)
        await ctx.send(embed=UserEmbed(member, **info, joined=joined))
