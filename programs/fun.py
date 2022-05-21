import discord
from discord.ext import commands

class fun(commands.Cog, name = "Welcome"):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "💚" and user.name != "westernfrog":
            channel = reaction.message.channel
            await channel.send("wow aagyiii ree")
            
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("sweam"):
            await message.channel.send("nice name")
        
          
def setup(bot):
    bot.add_cog(fun(bot))