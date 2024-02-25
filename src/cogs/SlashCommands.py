import random
import discord
import mysql.connector
import src.config as env
from discord import app_commands
from discord.ext import commands

db = mysql.connector.connect(
    host=env.DB_HOST,
    user=env.DB_USER,
    password=env.DB_PASSWORD,
    database=env.DB_NAME
)
dbcursor = db.cursor()

class SlashCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name='sync', description='Synchronizes commands with Discord')
  async def sync(self, interaction: discord.Interaction):
    if interaction.user.id == 550015170542567434:
        try:
            synced = await self.bot.tree.sync()
            # TODO: Add logs
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)

  @app_commands.command(name='version', description="Displays bot version and discord.py version")
  async def version(self, interaction: discord.Interaction):
    embed = discord.Embed(
      color=discord.Color.purple(),
      description=f'discord.py version: {discord.version_info.index}\nBot version: 1.0',
      title='Version'
    )
    embed.set_author(name='BreadBot', url='https://rope.com/')

    await interaction.response.send_message(embed=embed)

  @app_commands.command(name='russianroulette', description='When gabling you can lose only 100% BUT WIN 1000%')
  async def russianRoulette(self, interaction: discord.Interaction):
    if random.randrange(0, 6) == 1:
        await interaction.response.send_message('https://media1.tenor.com/m/1OlfIR9Mh-gAAAAd/face-in-the-lap-face.gif')
    else:
        await interaction.response.send_message('https://media1.tenor.com/m/N0MNEV-5or4AAAAC/chipi-chipi-chipi.gif')
  
  @app_commands.command(name='test', description="Used in development")
  async def test(self, interaction: discord.Interaction):
     await interaction.response.send_message("Why are you using it :3")

  # @app_commands.command(name='kys')
  # async def send_message(ctx, user: discord.User, *, message: str):
  #   """
  #   Sends a message to the mentioned user.
  #   Usage: !send_message @username Your message here
  #   """
  #   try:
  #       # Send the message to the mentioned user
  #       await user.send(message)
  #       await ctx.send(f"Message sent to {user.mention}: {message}")
  #   except discord.Forbidden:
  #       await ctx.send(f"Unable to send a message to {user.mention}. Make sure they allow DMs from this server.")

async def setup(bot):
  await bot.add_cog(SlashCommands(bot))