import discord


class Embed(discord.Embed):
    def __init__(self, title: str, description: str, color: discord.Color) -> None:
        super().__init__(title=title, description=description, color=color)


class KickEmbed(Embed):
    def __init__(self, member: discord.Member):
        super().__init__("", f"Kicked {member.mention}", discord.Color.orange())
