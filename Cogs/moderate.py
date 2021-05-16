import asyncio

import discord
from discord.ext import commands


class Kick(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason: str = None) -> None:
        await member.kick(reason=reason)
        await ctx.send(embed=discord.Embed(color=discord.Color.orange(), description=f"Kicked {member.mention}"))


class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason: str = None) -> None:
        await member.ban(reason=reason)
        await ctx.send(embed=discord.Embed(color=discord.Color.red(), description=f"Banned {member.mention}"))

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx: commands.Context, *, member: str) -> None:
        banned_user: list[discord.Member] = await ctx.guild.bans()

        for user in banned_user:
            if (user.user.name, user.user.discriminator) == (*member.split("#"),):
                await user.unban()
                await ctx.send(embed=discord.Embed(color=discord.Color.green(), description=f"Unbanned {user.mention}"))
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
        await member.add_roles(role, reason=reason)
        await asyncio.sleep(delay * 60)
        await member.remove_roles(role)

    @mute.error
    async def mute_error(self, ctx: commands.Context, error) -> None:
        if isinstance(error, commands.RoleNotFound):
            await ctx.guild.create_role(name="Muted",
                                        permissions=discord.Permissions(read_message_history=True, read_messages=True))
