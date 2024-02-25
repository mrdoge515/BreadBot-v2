import discord
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

class Events(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print(f'{self.bot.user} just went online!')
    await self.bot.change_presence(status=discord.Status.idle)

  @commands.Cog.listener()
  async def on_member_join(self, member):
    try:
      sql = "INSERT INTO test_users (dc_id, guild_id, lvl, kys_count, kms_count) VALUES (%s, %s, 0, 0, 0)"
      val = (member.id, member.guild.id,)
      dbcursor.execute(sql, val)
      db.commit()
    except Exception as e:
      # TODO: Add to logs
      print(f"Error processing member {member.id}: {e}")

async def setup(bot):
  await bot.add_cog(Events(bot))