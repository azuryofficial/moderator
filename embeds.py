import discord


class Embed:
    def __init__(self, color: int, description: str) -> None:
        self.embed = {"color:": color, "description": description}


class KickEmbed(Embed):
    def __init__(self, member: discord.Member) -> None:
        super().__init__(15105570, f"Kicked {member.mention}")
