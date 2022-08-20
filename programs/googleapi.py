import discord
from discord.ext import commands
from serpapi import GoogleSearch
import random

class googleapi(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command()
    async def image(self, ctx, *args):
        message = '+'.join(args)
        params = {
          "q": message,
          "tbm": "isch",
          "ijn": "0",
          "api_key": "477698bdf2954936a202befb298d84c929860ccd2e18b4ea5bf994bfda3718d6"
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        images_results = results['images_results']
        
        randoms = random.randint(0, len(images_results))
        await ctx.send(images_results[randoms]['original'])
        
        
def setup(bot):
    bot.add_cog(googleapi(bot))