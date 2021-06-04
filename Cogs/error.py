import logging

import discord
from discord.ext import commands

from misc import ErrorEmbed, replace_placeholders
from misc.config import ERRORS

__all__: list[str] = ["Error"]


class Error(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error) -> None:
        if isinstance(error, commands.CommandNotFound):
            replacement: dict = {"{command}": error.args[0].split()[1]}
            logging.error(replace_placeholders(ERRORS["CNF"].log, replacement))
            await ctx.send(embed=ErrorEmbed(replace_placeholders(ERRORS["CNF"].embed, replacement)))

        elif isinstance(error, commands.MissingRequiredArgument):
            replacement: dict = {"{command}": str(ctx.command), "{argument}": error.args[0].split()[0]}
            logging.info(replace_placeholders(ERRORS["MRA"].log, replacement))
            await ctx.send(embed=ErrorEmbed(replace_placeholders(ERRORS["MRA"].embed, replacement)))

        elif isinstance(error, commands.RoleNotFound):
            logging.error(f"The role {error.args[0].split()[1]} did not exist and was automatically created")
            await ctx.send(embed=ErrorEmbed("Missing role was automatically created. Try again."))
            if "Muted" in error.args[0]:
                await ctx.guild.create_role(name="Muted",
                                            permissions=discord.Permissions(read_message_history=True,
                                                                            read_messages=True),
                                            reason="Automatically created role for mute command.")

        elif isinstance(error, commands.MemberNotFound):
            logging.info(f"The member {error.args[0]} was not found.")
            await ctx.send(embed=ErrorEmbed("The member is not on this server."))

        else:
            logging.error(error)
