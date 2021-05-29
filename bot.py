import logging

from discord.ext import commands
from dotenv import dotenv_values

from Cogs import Kick, Ban, Mute, Error, Warn

bot: commands.Bot = commands.Bot("m.")
bot.remove_command("help")

bot.add_cog(Kick(bot))
bot.add_cog(Ban(bot))
bot.add_cog(Mute(bot))
bot.add_cog(Warn(bot))
bot.add_cog(Error())

if __name__ == "__main__":
    logging.basicConfig(filename="log.log", format="[%(asctime)s]:%(levelname)s:%(message)s",
                        datefmt="%H:%M:%S %d.%m.%Y", level=logging.WARNING)

    bot.run(dotenv_values(".env")["TOKEN"])
