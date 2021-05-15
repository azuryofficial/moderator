import discord
from discord.ext import commands

import embeds


class Kick(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason: str = None) -> None:
        await member.kick(reason=reason)
        await ctx.send(embed=discord.Embed().from_dict(embeds.KickEmbed(member).embed))


class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason: str = None) -> None:
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx: commands.Context, *, member: str) -> None:
        banned_user: list[discord.Member] = await ctx.guild.bans()

        for user in banned_user:
            if (user.user.name, user.user.discriminator) == (*member.split("#"),):
                await user.unban()
                break


class Warn(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx: commands.Context, member: discord.Member, *, reason: str = None) -> None:
        pass
