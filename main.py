import os
import discord
from dotenv import load_dotenv
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


@bot.tree.command(name='version')
async def version(interaction: discord.Interaction):
    embed = discord.Embed(
        color=discord.Color.purple(),
        description=f'discord.py version: {discord.version_info}\nBot version: 1.0',
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

bot.run(os.getenv('TOKEN'))