from BotConstants import getToken
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

# Base Variables
threadPrefix = "lfg"

# Create Diszcord Bot with proper permissions
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Login Logger
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

# # On Message Recieved
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print("test")
    await bot.process_commands(message)
#     if message.content.startswith("test"):
#         await message.channel.send("hi")

#     if message.content.startswith(threadPrefix) and message.channel.type == discord.ChannelType.text:
#         title = "Default Title"
#         boss = "N/A"
#         if len(threadPrefix) < len(message.content):
#             title = message.content[len(threadPrefix):]
#             boss = title
#         thread = await message.create_thread(name=title)
#         if boss != "N/A":
#             embed=discord.Embed(title=boss, url="https://fakelink.com/", description="Information goes here", color=0xFF5733)
#             await thread.send("Here is data on the boss: `" + boss + "`", embed=embed)
#         else:
#             await thread.send("No boss was located")

@bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)

bot.run(getToken())