import asyncio

import discord
import motor.motor_asyncio as motor
from discord.ext import commands

from misc import (
    CommandEmbed,
    add_entry,
    replace_placeholders,
)
from misc.config import COMMANDS

__all__: list[str] = ["Mute"]


class Mute(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db

    @commands.command(aliases=["m"])
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx: commands.Context, member: discord.Member, time: int = 1, *, reason: str = None) -> None:
        role: discord.Role = await commands.RoleConverter().convert(ctx, "Muted")
        await member.add_roles(role, reason=reason)
        await add_entry(self.db, COMMANDS["MUTE"].collection, ctx.message.author, member, reason)

        replacement: dict = {"{member}": member.mention, "{time}": time, "{reason}": reason or ""}
        await ctx.send(embed=CommandEmbed(
            replace_placeholders(COMMANDS["MUTE"].title, replacement),
            replace_placeholders(COMMANDS["MUTE"].description, replacement),
            member,
        ))

        await asyncio.sleep(time * 60)
        await member.remove_roles(role)
