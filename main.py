import os
import asyncio
import discord
import src.config as env
from discord.ext import commands

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')

async def load():
    for filename in os.listdir('./src/cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'src.cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start(env.DC_TOKEN)

asyncio.run(main())