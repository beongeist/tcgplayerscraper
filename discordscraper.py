import config
import discord
from discord.ext import commands
import mysql.connector


TOKEN = config.my_token
CHANNEL_ID = config.my_channel_ID

intents = discord.Intents.all()
intents.typing = False

bot = commands.Bot(command_prefix="!", intents=intents)


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='',
    database = 'tcgDB'
)

cursor = mydb.cursor(dictionary=True)


@bot.event
async def on_ready():
    print("TCGBuddy Combat Ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("TCGBuddy Online!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello")

@bot.command()
async def add(ctx, card):
    sql = "INSERT into users (ID, CARDS) VALUES (%s, %s)"
    val = (ctx.author.id, str(card))
    cursor.execute(sql, val)

@bot.command()
async def tracked(ctx):
    sql = f"SELECT CARDS from users where ID = {ctx.author.id}"
    result = cursor.fetchone()[1]
    await ctx.send(f"{result}")


bot.run(TOKEN)
