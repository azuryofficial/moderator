from discord.ext import commands
from dotenv import dotenv_values

from Cogs import Commands

bot: commands.Bot = commands.Bot("m.")
bot.remove_command("help")

bot.add_cog(Commands(bot))

if __name__ == "__main__":
    bot.run(dotenv_values(".env")["TOKEN"])
