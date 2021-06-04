import asyncio

import discord
import motor.motor_asyncio as motor
from discord.ext import commands

from misc import CommandEmbed, add_entry, replace_placeholders
from misc.config import COMMANDS

__all__: list[str] = ["Ban"]


class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, member: discord.Member, time: int, *, reason: str = None) -> None:
        await member.ban(reason=reason)
        replacement: dict = {"{member}": member.mention, "{reason}": reason, "{time}": time}
        await ctx.send(embed=CommandEmbed(replace_placeholders(COMMANDS["BAN"].title, replacement),
                                          replace_placeholders(COMMANDS["BAN"].description, replacement),
                                          member))
        await add_entry(self.db, "bans", ctx.message.author, member, reason)
        await asyncio.sleep(86400 * time)
        await member.unban()

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx: commands.Context, *, member: str) -> None:
        banned_user: list[discord.Member] = await ctx.guild.bans()

        for user in banned_user:
            if (user.user.name, user.user.discriminator) == (*member.split("#"),):
                await user.unban()
                replacement: dict = {"{member}": user.mention}
                await ctx.send(embed=CommandEmbed(replace_placeholders(COMMANDS["UNBAN"].title, replacement),
                                                  replace_placeholders(COMMANDS["UNBAN"].description, replacement),
                                                  user))
                break
