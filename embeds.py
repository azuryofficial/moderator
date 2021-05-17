import discord


class Embed(discord.Embed):
    def __init__(self, title: str, description: str, color: discord.Color) -> None:
        super().__init__(title=title, description=description, color=color)


class CommandEmbed(Embed):
    def __init__(self, method: str, member: discord.Member) -> None:
        super().__init__("", f"{method} {member.mention}", discord.Color.orange())
