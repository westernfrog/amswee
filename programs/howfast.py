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
            
            def check(reaction, user):
                return str(reaction.emoji) == '💛' and user != self.bot.user
            
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30, check=check)
                win = Embed(description=f'**{user.name}** reacted first and won  🎠✨', color=0x9b59b6)
                await ctx.send(embed=win)
            
            except asyncio.TimeoutError:
                await ctx.send("> you ran out of time!")
                    
def setup(bot):
    bot.add_cog(howfast(bot))