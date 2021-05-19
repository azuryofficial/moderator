import discord


class Embed:
    def __init__(self, title: str, description: str, color: discord.Color, member: discord.Member = None) -> None:
        self.embed: dict = {
            "author": {
                "name": member.display_name if member else "",
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
    def __init__(self, title: str, member: discord.Member) -> None:
        super().__init__(f"{title}", "", discord.Color.green(), member)


class ErrorEmbed(Embed):
    def __init__(self, description: str) -> None:
        super().__init__(":x: Error", description, discord.Color.red())
