from templatebot import Bot
from discord.ext import commands


class Profile(commands.Cog):
  def __init__(self, bot: Bot):
    self.bot = bot


def setup(bot: Bot):
  bot.add_cog(Profile(bot))
