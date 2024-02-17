import discord

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

    if message.content == 'Bread 👍':
        await message.channel.send('Bread 👍')

    if message.content == 'good bot':
        await message.channel.send('thanks bbg :3')

client.run('')