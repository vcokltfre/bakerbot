from templatebot import Bot
from discord.ext import commands
from re import compile

userre = compile(r"\b(<@!?[\d]{17,20}>|\d{17,20})\b")
numre = compile(r"\d+")


def find_id(text: str):
    a = numre.search(text).group()
    return int(a) if a else None


class Dev(commands.Cog, command_attrs=dict(hidden=True)):
    """Developer commands for BakerBot"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(name="status", aliases=["about", "info"])
    async def status(self, ctx: commands.Context):
        await ctx.send(
            f"BakerBot version {self.bot.VERSION}\nDevelopers: vcokltfre#6868, elf#2169"
        )

    @commands.command(name="hardreset")
    @commands.is_owner()
    async def hardreset(self, ctx: commands.Context):
        await self.bot.db.hardreset()
        await ctx.send("Database has been reset.")

    @commands.command(name="ban")
    @commands.is_owner()
    async def ban(self, ctx: commands.Context, id: str):
        id = find_id(id)
        if not id:
            return await ctx.reply("User not found.")
        await self.bot.db.ban_user(id)
        await self.bot.db.delete_bakery(id)
        await ctx.reply("User has been banned, and their bakery deleted.")

    @commands.command(name="unban")
    @commands.is_owner()
    async def unban(self, ctx: commands.Context, id: str):
        id = find_id(id)
        if not id:
            return await ctx.reply("User not found.")
        await self.bot.db.unban_user(id)
        await ctx.reply("User has been unbanned.")


def setup(bot: Bot):
    bot.add_cog(Dev(bot))
