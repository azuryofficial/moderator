from discord.ext import commands
from dotenv import dotenv_values

bot: commands.Bot = commands.Bot("m.")
bot.remove_command("help")

if __name__ == "__main__":
    bot.run(dotenv_values(".env")["TOKEN"])
