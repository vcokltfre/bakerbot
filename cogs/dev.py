from templatebot import Bot
from discord.ext import commands


class Dev(commands.Cog):
    """Developer commands for BakerBot"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(name="status")
    async def status(self, ctx: commands.Context):
        await ctx.send(f"BakerBot version {self.bot.VERSION}\nDevelopers: vcokltfre#6868, elf#2169")


def setup(bot: Bot):
  bot.add_cog(Dev(bot))
