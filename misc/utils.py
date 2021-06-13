from typing import Type

import motor.motor_asyncio as motor
from discord.ext import commands

__all__: list[str] = ["add_cogs", "replace_placeholders"]


def add_cogs(db: motor.AsyncIOMotorDatabase, bot: commands.Bot, cogs: list[Type[commands.Cog]]) -> None:
    for cog in cogs:
        bot.add_cog(cog(bot, db))


def replace_placeholders(string: str, replacements: dict) -> str:
    for original, replacement in replacements.items():
        string = string.replace(original, replacement)

    return string
