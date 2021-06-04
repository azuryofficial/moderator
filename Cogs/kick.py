import discord
import motor.motor_asyncio as motor
from discord.ext import commands

from misc import CommandEmbed, add_entry, replace_placeholders
from misc.config import COMMANDS

__all__: list[str] = ["Kick"]


class Kick(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason: str = None) -> None:
        await member.kick(reason=reason)
        replacement: dict = {"{member}": member.mention}
        await ctx.send(embed=CommandEmbed(replace_placeholders(COMMANDS["KICK"].title, replacement),
                                          replace_placeholders(COMMANDS["KICK"].description, replacement),
                                          member))
        await add_entry(self.db, COMMANDS["KICK"].collection, ctx.message.author, member, reason)
