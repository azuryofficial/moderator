from discord.ext import commands


class Error(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error) -> None:
        pass
