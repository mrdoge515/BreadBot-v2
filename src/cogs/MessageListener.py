import mysql.connector
import src.config as env
from discord.ext import commands

db = mysql.connector.connect(
    host=env.DB_HOST,
    user=env.DB_USER,
    password=env.DB_PASSWORD,
    database=env.DB_NAME
)
dbcursor = db.cursor()

class MessageListener(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.bot:
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
        sql = "UPDATE test_users SET kys_count = kys_count + 1 WHERE dc_id = %s AND guild_id = %s"
        val = (message.author.id, message.guild.id,)
        dbcursor.execute(sql, val)
        db.commit()
        dm_channel = await message.author.create_dm()
        await dm_channel.send("Need help?\nhttps://bron-sklep.pl/7-bron-krotka-/17-centralny-zaplon-/1108-glock-19-gen-5-kal-9x19-mm-.html")
        await message.add_reaction("👍🏿")

async def setup(bot):
  await bot.add_cog(MessageListener(bot))