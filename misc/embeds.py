import discord

from misc.config import COMMANDS

__all__: list[str] = ["CommandEmbed", "ErrorEmbed", "UserEmbed"]


class Embed(discord.Embed):
    def __init__(self, title: str, description: str, color: discord.Color, member: discord.Member = None) -> None:
        self.embed: dict = {
            "author": {
                "name": f"{member.name}#{member.discriminator}" if member else "",
                "icon_url": str(member.avatar_url) if member else "",
            },
            "title": title,
            "description": description,
            "color": color.value,
            "type": "rich",
        }

    def to_dict(self) -> dict:
        return self.embed


class CommandEmbed(Embed):
    def __init__(self, title: str, description: str, member: discord.Member) -> None:
        super().__init__(f"{title}", description, discord.Color.green(), member)


class ErrorEmbed(Embed):
    def __init__(self, description: str) -> None:
        super().__init__(":x: Error", description, discord.Color.red())


class UserEmbed(discord.Embed):
    def __init__(self, member: discord.Member, **kwargs) -> None:
        self.embed: dict = {
            "author": {
                "name": f"{member.name}#{member.discriminator}",
                "icon_url": str(member.avatar_url),
            },
            "title": COMMANDS["USER"].title,
            "description": COMMANDS["USER"].description,
            "fields": [
                {
                    "name": COMMANDS["USER"].joined,
                    "value": str(kwargs["joined"]),
                },
                {
                    "name": COMMANDS["USER"].bans,
                    "value": str(kwargs["bans"]),
                },
                {
                    "name": COMMANDS["USER"].kicks,
                    "value": str(kwargs["kicks"]),
                },
                {
                    "name": COMMANDS["USER"].mutes,
                    "value": str(kwargs["mutes"]),
                },
                {
                    "name": COMMANDS["USER"].warns,
                    "value": str(kwargs["warns"]),
                },
            ],
            "color": discord.Color.blurple().value,
            "type": "rich",
        }

    def to_dict(self):
        return self.embed
