import collections
from typing import Union

import discord
import discord.errors
import motor.motor_asyncio as motor
from discord.ext import commands

from misc import (
    CommandEmbed,
    add_entry,
    replace_placeholders,
)
from misc.config import COMMANDS

__all__: list[str] = ["Kick", "_kick"]


async def _kick(db: motor.AsyncIOMotorDatabase, author: Union[discord.Member, collections.namedtuple],
                member: discord.Member, reason: str) -> None:
    try:
        await member.kick(reason=reason)
    except discord.errors.Forbidden:
        pass

    await add_entry(db, COMMANDS["KICK"].collection, author, member, reason)


class Kick(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db

    @commands.command(aliases=["k"])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason: str = None) -> None:
        await _kick(self.db, ctx.message.author, member, reason)

        replacement: dict = {"{member}": member.mention, "{reason}": reason or ""}
        await ctx.send(embed=CommandEmbed(
            replace_placeholders(COMMANDS["KICK"].title, replacement),
            replace_placeholders(COMMANDS["KICK"].description, replacement),
            member,
        ))
