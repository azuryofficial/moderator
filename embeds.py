import discord


class Embed(discord.Embed):
    def __init__(self, title: str, description: str, color: discord.Color) -> None:
        super().__init__(title=title, description=description, color=color)


class CommandEmbed(Embed):
    def __init__(self, method: str, member: discord.Member) -> None:
        super().__init__(":white_check_mark: Success", f"{method} {member.mention}", discord.Color.green())


class ErrorEmbed(Embed):
    def __init__(self, description: str) -> None:
        super().__init__(":x: Error", description, discord.Color.red())
