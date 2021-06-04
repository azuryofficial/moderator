import logging

import discord
from discord.ext import commands

from misc.embeds import ErrorEmbed

__all__: list[str] = ["Error"]


class Error(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error) -> None:
        if isinstance(error, commands.CommandNotFound):
            logging.error(f"The {error.args[0].split()[1]} command does not exist")
            await ctx.send(embed=ErrorEmbed("This command does not exist."))

        elif isinstance(error, commands.MissingRequiredArgument):
            logging.info(f"The \"{ctx.command}\" command requires the  missing argument \"{error.args[0].split()[0]}\"")
            await ctx.send(embed=ErrorEmbed(f"You have to specify a {error.args[0].split()[0]}."))

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
