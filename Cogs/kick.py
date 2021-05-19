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
        await ctx.send(embed=CommandEmbed(":door: Kicked", member))
