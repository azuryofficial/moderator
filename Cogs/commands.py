import discord
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, user: discord.Member, *, reason: str = None) -> None:
        await user.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, user: discord.Member, *, reason: str = None) -> None:
        await user.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx: commands.Context, *, user: str) -> None:
        bans: list[discord.Member] = await ctx.guild.bans()

        for ban in bans:
            if (ban.user.name, ban.user.discriminator) == (*user.split("#"),):
                await ban.unban()
                break
