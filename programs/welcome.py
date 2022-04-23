import discord
from discord.ext import commands
import aiohttp
import random

class welcome(commands.Cog, name = "Welcome"):
    
    def __init__(self, bot):
        self.bot = bot
            
    @commands.Cog.listener()
    async def on_member_join(self, member):
        async with aiohttp.ClientSession() as cs:
                animals = ["dog","cat","panda","fox","koala","birb"]
                ani = random.choice(animals)
                async with cs.get("https://some-random-api.ml/img/"+ani) as r:
                    data = await r.json()
                    
        e = discord.Embed(title= ani+" welcomes !! you", description=f"{member.name} has joined the server", color=discord.Color.purple())
        e.set_thumbnail(url=member.avatar_url)       
        e.set_image(url=data['link'])
        channel = self.bot.get_channel(889003570890952737)
        msgg = await channel.send(embed = e)
        await msgg.add_reaction('💗')
        
    @commands.command()
    async def nick(self, ctx, m:discord.Member, *, newnick):
      await m.edit(nick=newnick)
      e=discord.Embed(title="Nickname is now set to "+newnick, color=discord.Color.purple())
      e.set_thumbnail(url=m.avatar_url)
      await ctx.send(embed=e)
        
def setup(bot):
    bot.add_cog(welcome(bot))
    
    
