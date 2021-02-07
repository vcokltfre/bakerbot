from templatebot import Bot
from discord.ext import commands
from json import load
from pathlib import Path

recipe_template = """Recipe for {item}
Produces: {prod}

This recipe requires:
{req}
"""


class Recipe(commands.Cog):
    """Calculate recipes"""

    def __init__(self, bot: Bot):
        self.bot = bot

        with Path("./static/recipes.json").open() as f:
            self.recipes = load(f)

    def get_recipe(self, name: str):
        for recipe in self.recipes:
            if recipe["name"] == name:
                return recipe
        return None

    @commands.command(name="recipe")
    async def recipe(self, ctx: commands.Context, *, item: str):
        r = self.get_recipe(item.lower())

        if not r:
            return await ctx.send(
                "I searched far and wide, but sadly I couldn't find that recipe :("
            )

        req = "\n".join([f"{i['amount']} {i['name']}" for i in r["ingredients"]])

        await ctx.send(
            recipe_template.format(item=item, prod=r["produces"]["human"], req=req)
        )


def setup(bot: Bot):
    bot.add_cog(Recipe(bot))
