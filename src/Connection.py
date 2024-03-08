from BotConstants import getToken
import discord

# Base Variables
threadPrefix = "lfg"

# Create Diszcord Bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Login Logger
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

# On Message Recieved
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("test"):
        await message.channel.send("hi")

    if message.content.startswith(threadPrefix) and message.channel.type == discord.ChannelType.text:
        title = "Default Title"
        boss = "N/A"
        if len(threadPrefix) < len(message.content):
            title = message.content[len(threadPrefix):]
            boss = title
        thread = await message.create_thread(name=title)
        if boss != "N/A":
            embed=discord.Embed(title=boss, url="https://fakelink.com/", description="Information goes here", color=0xFF5733)
            await thread.send("Here is data on the boss: `" + boss + "`", embed=embed)
        else:
            await thread.send("No boss was located")

client.run(getToken())