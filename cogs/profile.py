from templatebot import Bot
from discord import Embed
from discord.ext import commands
from re import compile
from asyncio import sleep

validname = compile(r"[a-zA-Z0-9_ ]{1,64}")


class Profile(commands.Cog):
    """The core commands for BakerBot"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(name="start", help="Start your adventure!", aliases=["begin"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def signup(self, ctx: commands.Context):
        resp = await self.bot.db.create_user(ctx.author.id, str(ctx.author))

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        banned = False
        bakery = None
        if not resp:
            banned = (await self.bot.db.get_user_id(ctx.author.id))[4]
            bakery = await self.bot.db.get_bakery_id(ctx.author.id)

        if banned:
            return await ctx.reply(
                "You are banned from using BakerBot for violating our bot's guidelines, therefore you're unable to create any more bakeries."
            )

        if bakery:
            return await ctx.reply("Sorry, you can't have more then 1 bakery.")

        base = await ctx.reply("Starting bakery creation process...")
        await sleep(0.75)
        await base.edit(content="What would you like to name your bakery?")

        try:
            resp = await self.bot.wait_for("message", check=check, timeout=30.0)
        except:
            return await base.edit(
                content="The selection timed out. Please run start again in a little while."
            )

        if not validname.match(resp.content):
            return await base.edit(
                content="That's not a valid name. Names must be alphanumeric and spaces, and be between 1 and 64 characters. Please run start again in a little while."
            )

        name = resp.content
        resp = await self.bot.db.create_bakery(ctx.author.id, name)
        await self.bot.logger.info(
            f"User {ctx.author} ({ctx.author.id}) created a bakery called {name}."
        )

        await ctx.send(
            f"You have created a bakery called {name}, you've been given 250h to start out, spend it well! Here's to many days of baking fun :cupcake:"
        )

    @commands.command(name="close")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def close(self, ctx: commands.Context):
        bakery = await self.bot.db.get_bakery_id(ctx.author.id)

        if not bakery:
            return await ctx.reply("You don't have a bakery to close!")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        base = await ctx.reply(
            "Are you sure you wish to close your bakery? This action is irreversible and permanent. Type `yes` to proceed."
        )
        try:
            resp = await self.bot.wait_for("message", check=check, timeout=30.0)
        except:
            return await base.edit(content="Timed out.")

        if resp.content.lower() == "yes":
            await self.bot.db.delete_bakery(ctx.author.id)
            await self.bot.logger.info(
                f"User {ctx.author} ({ctx.author.id}) deleted their bakery."
            )

            return await base.edit(content="Your bakery has been closed :(")

        await base.edit(content="Cancelled.")

    @commands.command(name="me", aliases=["bakery"], help="View your bakery.")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def me(self, ctx: commands.Context):
        user = await self.bot.db.get_user_id(ctx.author.id)
        bakery = await self.bot.db.get_bakery_id(ctx.author.id)

        if (not user) or not bakery:
            return await ctx.reply(
                "You haven't started a bakery yet! Start one now using b!start"
            )

        name = bakery[1]
        xp = bakery[4]
        h = bakery[5]

        embed = Embed(title=f"{ctx.author}'s Bakery", colour=0x87CEEB)
        embed.add_field(name="XP", value=str(xp))
        embed.add_field(name="Money", value=str(h) + "h")

        await ctx.reply(embed=embed)


def setup(bot: Bot):
    bot.add_cog(Profile(bot))
