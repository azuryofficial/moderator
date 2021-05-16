import discord


class Embed:
    def __init__(self, color: int, description: str) -> None:
        self.embed = {"color:": color, "description": description}


class KickEmbed:
    def __init__(self, member: discord.Member) -> None:
        self.embed = {"color": 15105570, "description": f"Kicked {member.mention}"}
