import discord
from discord.ext import commands
import datetime

import urllib.parse, urllib.request, re

#Bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=[">"], intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem impsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value="{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value="{ctx.guild.owner}")
    embed.add_field(name="Server Region", value="{ctx.guild.region}")
    embed.add_field(name="Server ID", value="{ctx.guild.idS}")
    embed.set_thumbnail(url="https://imgs.search.brave.com/DXokoDkfFfoCmzko0YXvyrkMrtrkyxWPRQ9odlLcoWE/rs:fit:476:225:1/g:ce/aHR0cHM6Ly90c2Uy/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5F/REo5eG9FckJiWnFL/MnRFeFZvSmZBSGFI/WSZwaWQ9QXBp")
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):

    query_string = urllib.parse.urlencode({'search_query': search})
    html_content =urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results=re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    await ctx.send('https://www.youtube.com/watch?=' + search_results[0])
 
#Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='Tutorials', url="http://www.twitch.tv/accountname"))
    print("My Bot is Ready")


bot.run('MTA1MTk4MTMyMzI4MTEwNDk4Ng.GWDhLQ.l6v_YWJPQfaFFCobTD2EWBfY5wWnAi7aPKXW7g')