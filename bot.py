import logging

from discord.ext import commands
from dotenv import dotenv_values

from misc.database import CLIENT

from Cogs import Kick, Ban, Mute, Error, Warn, User

bot: commands.Bot = commands.Bot("m.")
bot.remove_command("help")

bot.add_cog(Kick(bot, CLIENT.test))
bot.add_cog(Ban(bot, CLIENT.test))
bot.add_cog(Mute(bot, CLIENT.test))
bot.add_cog(Warn(bot, CLIENT.test))
bot.add_cog(User(bot, CLIENT.test))
bot.add_cog(Error())

if __name__ == "__main__":
    logging.basicConfig(filename="log.log", format="[%(asctime)s]:%(levelname)s:%(message)s",
                        datefmt="%H:%M:%S %d.%m.%Y", level=logging.WARNING)

    bot.run(dotenv_values(".env")["TOKEN"])
