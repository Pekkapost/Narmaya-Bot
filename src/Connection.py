from BotConstants import getToken
from HelpModule import MyHelpCommand
from CommandModule import FAQ, FarmData, Characters, CharBuild, Meme
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
# Logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename='output.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

class MyClient(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f"We have logged in as {self.user}")

    async def setup_hook(self) -> None:
        self.thread_cleanup.start()

    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            return
        logger.error(error)
        raise error
    
    async def on_raw_reaction_add(self, payload):
        if payload.member.bot:
            return
        message = await self.get_channel(payload.channel_id).fetch_message(payload.message_id)
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
            await message.create_thread(name=title,auto_archive_duration=60)

    async def on_message(self, message):
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

    @tasks.loop(minutes=1)
    async def thread_cleanup(self):
        for each in threadList:
            # Possible to fail to get channel
            try:
                currentChannel = await self.fetch_channel(each)
            except Exception as e:
                print("Could not find channel")
                logger.error(e)
                continue
            threads = currentChannel.threads
            # archivedThreads = await currentChannel.archived_threads()
            # for item in itertools.chain([threads,archivedThreads]):
            for item in threads:
                try:
                    message = await item.fetch_message(item.last_message_id)
                    newtime = (message.created_at - datetime.now(timezone.utc))
                    if newtime.total_seconds() < (-1 * (60 * 60 * 1)):
                        print("Deleting: "+ item.name)
                        await item.delete()
                except Exception as e:
                    print("Could not find message in thread")
                    logger.error(e)
                    pass

    @thread_cleanup.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()

async def main():
    # Setup Client
    intents = discord.Intents.default()
    intents.message_content = True
    listening = discord.Activity(type=discord.ActivityType.listening, name="Narmaya Bot | " + prefix)
    client = MyClient(command_prefix=prefix, intents=intents, case_insensitive=True, activity=listening, status=discord.Status.online)
    async with client:
        await client.add_cog(FAQ(client))
        await client.add_cog(FarmData(client))
        await client.add_cog(Characters(client))
        await client.add_cog(CharBuild(client))
        await client.add_cog(Meme(client))
        await client.start(getToken())

asyncio.run(main())