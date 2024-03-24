from BotConstants import getToken
from HelpModule import MyHelpCommand
import discord
from discord.ext.commands import Bot, CommandNotFound
import json
import os
import asyncio
from discord.ext import commands, tasks
from datetime import datetime, timezone
import logging
import itertools

# Load Variables
cwd = os.path.dirname(os.path.realpath(__file__))
varFile = open(cwd + "/GBFRdiscord.json")
varData = json.load(varFile)
# Set Variables
threadList = varData["threadList"]
prefix = varData["prefix"]
pingRoles = varData["pingRoles"]
emoteThread = varData["emoteThread"]
whitelist = varData["whitelist"]
# Logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename='output.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

class MyClient(Bot):
    # Init Function
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Called every time the bot connects (Disconnects will trigger this)
    async def on_ready(self):
        print(f"We have logged in as {self.user}")

    # Called once
    async def setup_hook(self) -> None:
        self.thread_cleanup.start()
        
        # Slash command sync function
        await self.tree.sync()

    # Ignore unfound commands
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            return
        # Safety error call
        logger.error(error)
        raise error
    
    # For LFG Automatic Threads
    async def on_raw_reaction_add(self, payload):
        # Ignore bots (self)
        if payload.member.bot:
            return
        # Check for any proper emote
        message = await self.get_channel(payload.channel_id).fetch_message(payload.message_id)
        emote = payload.emoji
        if str(emote) != emoteThread:
            return
        messageContent = message.content
        mentions = message.raw_role_mentions
        foundMention = False
        # Check for any proper role mention
        for roleMention in mentions:
            if roleMention in pingRoles:
                foundMention = True
            messageContent = messageContent.replace("<@&"+str(roleMention)+">","")
        # Trigger on found role
        if foundMention:
            title = message.author.name + "`s " + messageContent
            # Limit title length
            if len(title) > 80:
                title = title[:80]
            await message.create_thread(name=title,auto_archive_duration=60)

    async def on_message(self, message):
        # This does allow other bots
        if message.author == self.user:
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
        # Wait for command
        await self.process_commands(message)
    
    # Load all Cogs
    async def init_cogs(self):
        for file in os.listdir(f"{cwd}/cogs"):
            if file.endswith(".py"):
                name = file[0:-3]
                try:
                    await self.load_extension(f"cogs.{name}")
                except Exception as e:
                    print(f"Could not load {name} Cog!")
                    logger.error(f"{name} cog failed :")
                    logger.error(e)

    # Auto delete old threads
    @tasks.loop(hours=1)
    async def thread_cleanup(self):
        for each in threadList:
            # Ignore failing to get a channel
            try:
                currentChannel = await self.fetch_channel(each)
            except Exception as e:
                continue
            # Compile all threads into one list
            threads = currentChannel.threads
            archivedThreads = [athread async for athread in currentChannel.archived_threads()]
            iterList = [threads, archivedThreads]
            # Check thread for deletion
            for thread in itertools.chain(*iterList):
                # Ignore WR Lucilius Dicussion (Temporary)
                if thread.id in whitelist:
                    print("Skipping: " + str(thread.id))
                    continue
                # Attempt deletion
                try:
                    messages = [message async for message in thread.history(limit=1)]
                    newtime = (datetime.now(timezone.utc) - messages[0].created_at)
                    if newtime.total_seconds() > (1 * (60 * 60 * 1)):
                        print("Deleting: "+ thread.name)
                        await thread.delete()
                except Exception as e:
                    print("Could not find message in thread")
                    logger.error("Trying to find " + str(thread.last_message_id))
                    logger.error(e)

    # Wait for bot to be ready
    @thread_cleanup.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()

async def main():
    intents = discord.Intents.default()
    intents.message_content = True
    listening = discord.Activity(type=discord.ActivityType.listening, name="Narmaya Bot | " + prefix)
    client = MyClient(command_prefix=prefix, intents=intents, case_insensitive=True, activity=listening, status=discord.Status.online)
    async with client:
        await client.init_cogs()
        await client.start(getToken())

asyncio.run(main())