import collections

import discord
import motor.motor_asyncio as motor
from discord.ext import commands

from Cogs.warn import _warn
from misc import ErrorEmbed, CommandEmbed, add_word, delete_word, replace_placeholders
from misc.config import COMMANDS

__all__: list[str] = ["Censor"]


class Censor(commands.Cog):
    def __init__(self, bot: commands.Bot, db: motor.AsyncIOMotorDatabase) -> None:
        self.bot: commands.Bot = bot
        self.db: motor.AsyncIOMotorDatabase = db

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def censor(self, ctx: commands.Context, *, word: str) -> None:
        if not await add_word(self.db, word):
            await ctx.send(embed=ErrorEmbed("The word is already censored."))

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def permit(self, ctx: commands.Context, *, word: str) -> None:
        if not await delete_word(self.db, word):
            await ctx.send(embed=ErrorEmbed("The word is not censored."))

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        censored_words: collections.AsyncIterable = self.db[COMMANDS["CENSOR"].collection].find()
        async for word in censored_words:
            if word["_id"] in message.content.lower():
                await _warn(self.db, collections.namedtuple("Author", "id")(self.bot.user.id), message.author,
                            COMMANDS["CENSOR"].reason)
                replacement: dict = {"{member}": message.author.mention, "{reason}": COMMANDS["CENSOR"].reason or ""}
                await message.reply(embed=CommandEmbed(replace_placeholders(COMMANDS["CENSOR"].title, replacement),
                                                       replace_placeholders(COMMANDS["CENSOR"].description,
                                                                            replacement),
                                                       message.author))
