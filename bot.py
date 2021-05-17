from discord.ext import commands
from dotenv import dotenv_values

from Cogs import Kick, Ban, Mute, Error

bot: commands.Bot = commands.Bot("m.")
bot.remove_command("help")

bot.add_cog(Kick(bot))
bot.add_cog(Ban(bot))
bot.add_cog(Mute(bot))
bot.add_cog(Error())

if __name__ == "__main__":
    bot.run(dotenv_values(".env")["TOKEN"])
