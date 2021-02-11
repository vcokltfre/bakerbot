from templatebot import Bot
from discord.ext import commands
from json import loads, dumps

from utils.text import strip_backticks

recipe_template = """**__Recipe for {item}__**
Produces: {prod}

This recipe requires:
{req}

This item is worth **{value}h**
"""


class Recipe(commands.Cog):
    """Calculate recipes"""

    def __init__(self, bot: Bot):
        self.bot = bot

    async def get_recipe(self, name: str):
        r = await self.bot.db.get_recipe(name)

        if not r:
            return None

        return {
            "name": r[0],
            "produces": {"amount": r[1], "human": r[2]},
            "value": r[3],
            "ingredients": loads(r[4]),
        }

    @commands.command(name="recipe")
    async def recipe(self, ctx: commands.Context, *, item: str):
        r = await self.get_recipe(item.lower())

        if not r:
            return await ctx.send(
                "I searched far and wide, but sadly I couldn't find that recipe :("
            )

        req = "\n".join([f"{i['amount']} {i['name']}" for i in r["ingredients"]])

        await ctx.send(
            recipe_template.format(
                item=item, prod=r["produces"]["human"], req=req, value=r["value"]
            )
        )

    @commands.command(name="mkrecipe")
    @commands.is_owner()
    async def mkrecipe(self, ctx: commands.Context, *, json: str):
        json = loads(strip_backticks(json))
        name = json.get("name")
        value = json.get("value")
        qty = json.get("amount")
        human = json.get("human")
        ingredients = json.get("ingredients")

        await self.bot.db.create_recipe(name, qty, human, value, dumps(ingredients))
        await ctx.send("Recipe created!")


def setup(bot: Bot):
    bot.add_cog(Recipe(bot))
