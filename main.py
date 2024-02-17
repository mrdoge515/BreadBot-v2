import os
import re
import discord
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    match message.content.lower():
        case str(x) if 'bread 👍' in x:
            await message.channel.send('Bread 👍')
        case str(x) if 'good bot' in x:
            await message.channel.send('thanks bbg :3')

client.run(os.getenv("TOKEN"))