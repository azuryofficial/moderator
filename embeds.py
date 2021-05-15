import discord


class KickEmbed:
    def __init__(self, member: discord.Member) -> None:
        self.embed = {"color": 15105570, "description": f"Kicked {member.mention}"}
