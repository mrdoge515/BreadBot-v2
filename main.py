import os
import random
import discord
from dotenv import load_dotenv
import mysql.connector
from discord.ext import commands

load_dotenv()

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_f11479"
)
dbcursor = db.cursor()

@bot.event
async def on_ready():
    print(f'{bot.user} just went online!')
    await bot.change_presence(status=discord.Status.idle)

@bot.event
async def on_member_join(member):
    try:
        sql = "INSERT INTO users (dc_id, guild_id, lvl, kys_count, kms_count) VALUES (%s, %s, 0, 0, 0)"
        val = (member.id, member.guild.id,)
        dbcursor.execute(sql, val)
        db.commit()
    except Exception as e:
        # TODO: Add to logs
        print(f"Error processing member {member.id}: {e}")

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
        case str(x) if 'kys' in x:
            sql = "UPDATE users SET kys_count = kys_count + 1 WHERE dc_id = %s"
            val = (message.author.id,)
            dbcursor.execute(sql, val)
            db.commit()
            dm_channel = await message.author.create_dm()
            await dm_channel.send("Need help?\nhttps://bron-sklep.pl/7-bron-krotka-/17-centralny-zaplon-/1108-glock-19-gen-5-kal-9x19-mm-.html")
            await message.add_reaction("👍🏿")

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

@bot.tree.command(name='test')
async def test(interaction: discord.Interaction):
    print("test used")

@bot.tree.command(name='kys')
async def send_message(ctx, user: discord.User, *, message: str):
    """
    Sends a message to the mentioned user.
    Usage: !send_message @username Your message here
    """
    try:
        # Send the message to the mentioned user
        await user.send(message)
        await ctx.send(f"Message sent to {user.mention}: {message}")
    except discord.Forbidden:
        await ctx.send(f"Unable to send a message to {user.mention}. Make sure they allow DMs from this server.")

bot.run(os.getenv('TOKEN'))