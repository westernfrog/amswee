import discord
from discord.ext import commands, tasks
import aiohttp
import os
import random
import asyncio
import datetime


client = commands.Bot(command_prefix = "", intents = discord.Intents.all())

for folder in os.listdir("./programs"):
    if folder.endswith(".py"):
        client.load_extension(f'programs.{folder[:-3]}')


        
@tasks.loop(hours=7)
async def loop():
            async with aiohttp.ClientSession() as cs:
                animals = ["dog","cat"]
                animal = random.choice(animals)
                async with cs.get("https://some-random-api.ml/img/"+animal) as r:
                    today = datetime.date.today()
                    special_day = datetime.date(2022, 8, 6)
                    days_left = special_day - today
                    data = await r.json()
                    emojis = ["💞","💗","🧡","💛","💚","💙","💜","🤎","🖤","🤍","💓","💖","💟","💌","💝","💘","❣️"]
                    emoji = random.choice(emojis)
                    embed = discord.Embed(color=0x9b59b6)
                    embed.set_image(url=data['link'])
                    embed.set_footer(text=emoji+"This "+animal+" orders you to stay hydrated"+emoji+"\n"+emoji+str(days_left.days)+" days left for that special day!"+emoji)
                    channel = client.get_channel(889003570890952737)
                    await asyncio.sleep(5800)
                    await channel.send(embed=embed)
                             
                
@client.event
async def on_connect():
  print("bot is online")
  await client.change_presence(status=discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.listening, name="her, as she knows better"))
  loop.start()
	
	
@client.event
async def on_message(message):
  
  if message.content.startswith("i love you"):
    await message.add_reaction('💗')
  elif message.content.startswith("sorry"):
    msg = await message.channel.send("please forgive and forget it")
    await asyncio.sleep(5)
    await msg.delete()
  elif message.content.startswith("wel cum"):
    await message.add_reaction('💦')
  elif message.content.startswith("cum"):
    await message.add_reaction('🥵')
  elif message.content.startswith("swetha") or message.content.startswith("aman"):
    await message.add_reaction('💛')
    await message.add_reaction('🧡')
    await message.add_reaction('❤️')
    await message.add_reaction('💚')
    await message.add_reaction('💙')
    await message.add_reaction('💜')

  await client.process_commands(message)
    
token = ""

client.run(token)