import discord
from discord.ext import commands
import json
import os
import re

global dataFile, database
cwd = os.path.dirname(os.path.realpath(__file__))
dataFile = open(cwd + "/../Database.json")
database = json.load(dataFile)

class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    def getMeme(self, item):
        meme = database["meme"]
        return meme[item]["link"]

    @commands.command(
            help=database["meme"]["grind"]["help"],
            brief=database["meme"]["grind"]["help"]
    )
    async def grind(self, ctx):
        item = "grind"
        await ctx.send(self.getMeme(item))

async def setup(client):
    await client.add_cog(Meme(client))