from templatebot import Bot
from discord.ext import commands



class Utility(commands.Cog):
    """Utility commands"""
    
    def __init__(self, bot):
        self.bot = bot


    @commands.command
    async def about(self, ctx : commands.Context):
        await ctx.send("**About**\n\nBakery bot is a new exciting discord bot where you'll be able to start your own bakery from the ground and rise to the top, compete with other users as the most-skilled bakery, bake rare items, and have fun using our new bot!\n\nTo start using this bot, type `b!start`, and follow the walkthrough.")
        
        
        
        
def setup(bot):
    bot.add_cog(Utility(bot))
  
