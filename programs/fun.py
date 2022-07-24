import discord
from discord.ext import commands
from discord import Embed
import datetime
import pytz

class fun(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("days left") or message.content.startswith("day left"):
            today = datetime.date.today()
            special_day = datetime.date(2022, 8, 6)
            days_left = special_day - today
            date = Embed(description=f'Just **{days_left.days}** **days** left for that special, big day! ❤️❤️', color=0x9b59b6)
            msg = await message.channel.send(embed=date)
            await msg.add_reaction("😍")
            
        elif message.content.startswith("forever"):
            timezone = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
            time = timezone.strftime('%d %B, %A %I:%M %p')
            embed = discord.Embed(color=0x9b59b6)
            embed.set_image(url="https://media4.giphy.com/media/l3q2PwxrzxW6JseU8/giphy.gif?cid=ecf05e47kglutw2tjw52vy3x996rgll0juhz46dbebwrnq15&rid=giphy.gif&ct=g")
            embed.set_footer(text="We are together forever! ♾️ \n"+str(time))
            await message.channel.send(embed=embed)
            
   
def setup(bot):
    bot.add_cog(fun(bot))