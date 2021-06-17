import logging

from discord.ext import commands
from dotenv import dotenv_values

from Cogs import *
from misc import (
    CLIENT,
    add_cogs,
)

bot: commands.Bot = commands.Bot("m.")
bot.remove_command("help")

add_cogs(
    CLIENT.test,
    bot,
    [Kick, Ban, Mute, Warn, User, Setup, Censor, Spam],
)
bot.add_cog(Error())

if __name__ == "__main__":
    logging.basicConfig(
        filename="log.log",
        format="[%(asctime)s]:[%(levelname)s]:%(message)s",
        datefmt="%H:%M:%S %d.%m.%Y",
        level=logging.WARNING,
    )

    bot.run(dotenv_values(".env")["TOKEN"])
