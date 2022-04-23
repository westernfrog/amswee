import discord
from discord.ext import commands
from discord import Embed
import asyncio
import random

class howfast(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def howfast(self, ctx):
            first = Embed(description='3',color=0x9b59b6)
            second = Embed(description='2',color=0x9b59b6)
            third = Embed(description='1',color=0x9b59b6)
            fourth = Embed(description='react !!',color=0x9b59b6)
    
            msg = await ctx.send(embed=first)
            await asyncio.sleep(1)
            await msg.edit(embed=second) 
            await asyncio.sleep(1)
            await msg.edit(embed=third)
            await asyncio.sleep(2)
            await msg.edit(embed=fourth)
            await msg.add_reaction("💛")
            
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "💛" and user.name != "♡♡amswe♡♡":
            channel = reaction.message.channel
            win = Embed(title=f'{user.name} reacted first and won 🎉🎉', color=0x9b59b6)
            await channel.send(embed=win)
            
        

            
           
       
    
def setup(bot):
    bot.add_cog(howfast(bot))