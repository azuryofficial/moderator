from typing import Type

import motor.motor_asyncio as motor
from discord.ext import commands


def add_cogs(db: motor.AsyncIOMotorDatabase, bot: commands.Bot, cogs: list[Type[commands.Cog]]) -> None:
    for cog in cogs:
        bot.add_cog(cog(bot, db))
