import os
import random
import discord
from dotenv import load_dotenv
import mysql.connector
from discord.ext import commands

load_dotenv()

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} just went online!')
    await bot.change_presence(status=discord.Status.idle)
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    match message.content.lower():
        case str(x) if 'bread 👍' in x:
            await message.channel.send('Bread 👍')
        case str(x) if 'good bot' in x:
            await message.channel.send('thanks bbg :3')
            await message.channel.send('https://i.pinimg.com/originals/0a/c1/5c/0ac15c04eaf7264dbfac413c6ce11496.gif')
        case str(x) if 'way' in x:
            await message.channel.send("https://media1.tenor.com/m/vWK04T5bh4kAAAAd/zoro-miles-morales.gif")

@bot.tree.command(name='version')
async def version(interaction: discord.Interaction):
    embed = discord.Embed(
        color=discord.Color.purple(),
        description=f'discord.py version: {discord.version_info.index}\nBot version: 1.0',
        title='Version'
    )
    embed.set_author(name='BreadBot', url='https://mrdoge.xyz/')

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name='sync')
async def sync(interaction: discord.Interaction):
    if interaction.user.id == 550015170542567434:
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)

@bot.tree.command(name='russianroulette')
async def russianRoulette(interaction: discord.Interaction):
    number1 = random.randrange(0, 6)

    if random.randrange(0, 6) == 1:
        await interaction.response.send_message('https://media1.tenor.com/m/1OlfIR9Mh-gAAAAd/face-in-the-lap-face.gif')
    else:
        await interaction.response.send_message('https://media1.tenor.com/m/N0MNEV-5or4AAAAC/chipi-chipi-chipi.gif')




bot.run(os.getenv('TOKEN'))