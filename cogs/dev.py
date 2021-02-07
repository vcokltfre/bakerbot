from templatebot import Bot
from discord.ext import commands


class Dev(commands.Cog):
    """Developer commands for BakerBot"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(name="status", aliases=["about", "info"])
    async def status(self, ctx: commands.Context):
        await ctx.send(f"BakerBot version {self.bot.VERSION}\nDevelopers: vcokltfre#6868, elf#2169")

    @commands.command(name="hardreset")
    async def hardreset(self, ctx: commands.Context):
        await self.bot.db.hardreset()
        await ctx.send("Database has been reset.")

    @commands.command(name="ban")
    async def ban(self, ctx: commands.Context, id: int):
        await self.bot.db.ban_user(id)
        await ctx.reply("User has been banned.")

    @commands.command(name="unban")
    async def unban(self, ctx: commands.Context, id: int):
        await self.bot.db.unban_user(id)
        await ctx.reply("User has been unbanned.")


def setup(bot: Bot):
  bot.add_cog(Dev(bot))
