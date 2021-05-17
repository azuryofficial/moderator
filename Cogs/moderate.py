import asyncio

import discord
from discord.ext import commands

from embeds import CommandEmbed


class Kick(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason: str = None) -> None:
        await member.kick(reason=reason)
        await ctx.send(embed=CommandEmbed("Kicked", member))


class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason: str = None) -> None:
        await member.ban(reason=reason)
        await ctx.send(embed=CommandEmbed("Banned", member))

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx: commands.Context, *, member: str) -> None:
        banned_user: list[discord.Member] = await ctx.guild.bans()

        for user in banned_user:
            if (user.user.name, user.user.discriminator) == (*member.split("#"),):
                await user.unban()
                await ctx.send(embed=CommandEmbed("Unbanned", user))
                break


class Warn(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx: commands.Context, member: discord.Member, *, reason: str = None) -> None:
        pass


class Mute(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx: commands.Context, member: discord.Member, delay: int = 1, *, reason: str = None) -> None:
        role: discord.Role = await commands.RoleConverter().convert(ctx, "Muted")
        await ctx.send(embed=CommandEmbed("Muted", member))
        await member.add_roles(role, reason=reason)
        await asyncio.sleep(delay * 60)
        await member.remove_roles(role)
