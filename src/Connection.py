from BotConstants import getToken
from HelpModule import MyHelpCommand
from CommandModule import FAQ, FarmData, Characters, CharBuild, Meme
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import json
import os
import asyncio
import re

cwd = os.path.dirname(os.path.realpath(__file__))

# Load Variables
varFile = open(cwd + "/GBFRdiscord.json")
varData = json.load(varFile)
# Set Variables
threadList = varData["threadList"]
prefix = varData["prefix"]
pingRoles = varData["pingRoles"]
emoteThread = varData["emoteThread"]

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

@client.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        return
    message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    emote = payload.emoji
    if str(emote) != emoteThread:
        return
    messageContent = message.content
    mentions = message.raw_role_mentions
    foundMention = False
    for roleMention in mentions:
        if roleMention in pingRoles:
            foundMention = True
        messageContent = messageContent.replace("<@&"+str(roleMention)+">","")
    if foundMention:
        title = message.author.name + "`s " + messageContent
        if len(title) > 80:
            title = title[:80]
        await message.create_thread(name=title)

# # On Message Recieved
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # Check for LFG Command
    if message.channel.id in threadList and message.channel.type == discord.ChannelType.text:
        mentions = message.raw_role_mentions
        foundMention = False
        for roleMention in mentions:
            if roleMention in pingRoles:
                foundMention = True
        if foundMention:
            await message.add_reaction(emoteThread)
    # Wait for commands
    await client.process_commands(message)

async def main():
    async with client:
        await client.add_cog(FAQ(client))
        await client.add_cog(FarmData(client))
        await client.add_cog(Characters(client))
        await client.add_cog(CharBuild(client))
        await client.add_cog(Meme(client))
        await client.start(getToken())

asyncio.run(main())