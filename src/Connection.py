from BotConstants import getToken
from HelpModule import MyHelpCommand
from CommandModule import FAQ, FarmData, Characters
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import json
import os
import asyncio
import re

cwd = os.path.dirname(os.path.realpath(__file__))

# Load Variables
varFile = open(cwd + "\GBFRdiscord.json")
varData = json.load(varFile)
# Set Variables
threadPrefix = varData["threadPrefix"]
threadChannel = varData["threadChannel"]
prefix = varData["prefix"]
pingRoles = varData["pingRoles"]

# Setup Client
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True)
# client.help_command = MyHelpCommand()

# Login Logger
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

# Ignore command not found
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

# # On Message Recieved
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # Check for LFG Command
    if message.channel.id == threadChannel and message.content.startswith(threadPrefix) and message.channel.type == discord.ChannelType.text:
        mentions = message.raw_role_mentions
        title = "Default Title"
        foundMention = False
        messageContent = message.content[len(threadPrefix):]
        for roleMention in mentions:
            if roleMention in pingRoles:
                messageContent = messageContent.replace("<@&"+str(roleMention)+">","")
                foundMention = True
        if foundMention:
            title = message.author.name + "`s " + messageContent
        thread = await message.create_thread(name=title)
        # embed=discord.Embed(title=boss, url="https://fakelink.com/", description="Information goes here", color=0xFF5733)
        # await thread.send("Here is data on the boss: `" + boss + "`", embed=embed)

    # Wait for commands
    await client.process_commands(message)

async def main():
    async with client:
        await client.add_cog(FAQ(client))
        await client.add_cog(FarmData(client))
        await client.add_cog(Characters(client))
        await client.start(getToken())

asyncio.run(main())