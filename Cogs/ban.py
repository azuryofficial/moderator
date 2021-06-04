import discord
import motor.motor_asyncio as motor
from discord.ext import commands

from misc import add_entry
from misc.embeds import CommandEmbed

__all__: list[str] = ["Ban"]


class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason: str = None) -> None:
        await member.ban(reason=reason)
        await ctx.send(embed=CommandEmbed(":no_entry: Banned", member))
        await add_entry(self.db, "bans", ctx.message.author, member, reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx: commands.Context, *, member: str) -> None:
        banned_user: list[discord.Member] = await ctx.guild.bans()

        for user in banned_user:
            if (user.user.name, user.user.discriminator) == (*member.split("#"),):
                await user.unban()
                await ctx.send(embed=CommandEmbed(":wave: Unbanned", user))
                break
