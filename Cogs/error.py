import logging

import discord
from discord.ext import commands

from misc import (
    ErrorEmbed,
    replace_placeholders,
)
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

            logging.warning(replace_placeholders(ERRORS["MRA"].log, replacement))
            await ctx.send(embed=ErrorEmbed(replace_placeholders(ERRORS["MRA"].embed, replacement)))

        elif isinstance(error, commands.RoleNotFound):
            replacement: dict = {"{role}": error.args[0].split()[1]}

            logging.error(replace_placeholders(ERRORS["RNF"].log, replacement))
            await ctx.send(embed=ErrorEmbed(replace_placeholders(ERRORS["RNF"].embed, replacement)))

            if "Muted" in error.args[0]:
                await ctx.guild.create_role(
                    name="Muted",
                    permissions=discord.Permissions(read_message_history=True, read_messages=True),
                    reason="Automatically created role for mute command.",
                )

        elif isinstance(error, commands.MemberNotFound):
            replacement: dict = {"{member}": error.args[0]}

            logging.warning(replace_placeholders(ERRORS["MNF"].log, replacement))
            await ctx.send(embed=ErrorEmbed(replace_placeholders(ERRORS["MNF"].embed, replacement)))

        else:
            logging.error(error)
