import discord
from discord.ext import commands
import aiohttp
import praw
import random

reddit = praw.Reddit(client_id="",client_secret="",username="",password="",user_agent="",check_for_async=False)

class images(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def dogs(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/img/dog") as r:
                    data = await r.json()

                    embed = discord.Embed(color=0x9b59b6)
                    embed.set_image(url=data['link'])

                    await ctx.send(embed=embed)

    @commands.command()
    async def cats(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()
                    embed = discord.Embed(color=0x9b59b6)
                    embed.set_image(url=data['file'])

                    await ctx.send(embed=embed)

    @commands.command()
    async def birds(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/img/birb") as r:
                    data = await r.json()
                    embed = discord.Embed(color=0x9b59b6)
                    embed.set_image(url=data['link'])

                    await ctx.send(embed=embed)
                  
    
    @commands.command()
    async def meme(self, ctx):
      subreddit = reddit.subreddit("memes")
      all_subs = []
      hot = subreddit.hot()

      for submission in hot:
        all_subs.append(submission)

      random_sub = random.choice(all_subs)
      
      name = random_sub.title
      url = random_sub.url

      em = discord.Embed(title=name,color=0x9b59b6)
      em.set_image(url=url)
      await ctx.send(embed = em)
  
def setup(client):
    client.add_cog(images(client))
