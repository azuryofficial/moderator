import collections
from typing import Union

import discord
import motor.motor_asyncio as motor
from discord.ext import commands

from misc import CommandEmbed, add_entry, replace_placeholders
from misc.config import COMMANDS

__all__: list[str] = ["Warn", "_warn"]


async def _warn(db: motor.AsyncIOMotorDatabase, author: Union[discord.Member, collections.namedtuple],
                member: discord.Member, reason: str) -> None:
    await add_entry(db, COMMANDS["WARN"].collection, author, member, reason)


class Warn(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx: commands.Context, member: discord.Member, *, reason: str = None) -> None:
        replacement: dict = {"{member}": member.mention, "{reason}": reason or ""}
        await ctx.send(embed=CommandEmbed(replace_placeholders(COMMANDS["WARN"].title, replacement),
                                          replace_placeholders(COMMANDS["WARN"].description, replacement),
                                          member))
        await _warn(self.db, ctx.message.author, member, reason)
