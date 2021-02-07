from templatebot import Bot
from discord.ext import commands


class Utility(commands.Cog):
    """Utility commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def top(self, ctx: commands.Context):
      embed = discord.Embed(
        title = "Leaderboard",
        description = "Top 25 bot users.",
        color = 0x87CEEB)
      embed.add_field(name="Users", value=".") # TODO: add db stuff here


def setup(bot):
    bot.add_cog(Utility(bot))
