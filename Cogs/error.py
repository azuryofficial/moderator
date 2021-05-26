import logging

import discord
from discord.ext import commands

from utils.embeds import ErrorEmbed


class Error(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error) -> None:
        if isinstance(error, commands.CommandNotFound):
            logging.warning(f"CommandNotFound: {error.args[0]}")
            await ctx.send(embed=ErrorEmbed("This command does not exist."))

        elif isinstance(error, commands.MissingRequiredArgument):
            logging.error(f"MissingRequiredArgument: {error.args[0]}")
            if "member" in error.args[0]:
                await ctx.send(embed=ErrorEmbed("You have to specify a member."))

        elif isinstance(error, commands.RoleNotFound):
            logging.error(f"RequiredRoleNotFound: {error.args[0]}")
            await ctx.send(embed=ErrorEmbed("Missing role was automatically created. Try again."))
            if "Muted" in error.args[0]:
                await ctx.guild.create_role(name="Muted",
                                            permissions=discord.Permissions(read_message_history=True,
                                                                            read_messages=True),
                                            reason="Automatically created role for mute command.")

        else:
            logging.error(error)
