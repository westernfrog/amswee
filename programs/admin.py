import discord
from discord.ext import commands

class admin(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot 

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send("> could not unload cog")
            return
        await ctx.send("> cog unloaded")

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("> could not load cog")
            return
        await ctx.send("> cog loaded")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("> could not reload cog")
            return
        await ctx.send("> cog reloaded")
             
def setup(bot):
    bot.add_cog(admin(bot))