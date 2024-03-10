import discord
from discord.ext import commands
import json
import os
import re

global dataFile, database
cwd = os.path.dirname(os.path.realpath(__file__))
dataFile = open(cwd + "/Database.json")
database = json.load(dataFile)

class FarmData(commands.Cog):
    def __init__(self, client):
        self.client = client

    def getEmbed(self, item):
        faq = database["farmData"]
        data = faq[item]
        display = data["data"]
        link = ""
        if "link" in data:
            link = data["link"]
        img = ""
        if "image" in data:
            img = data["image"]
        embed=discord.Embed(title=item, url=link, description=display, color=0xa0a0ff)
        embed.set_thumbnail(url=img)
        return embed

    @commands.command(
            aliases=["terminus"],
            help=database["farmData"]["Terminus Weapon"]["help"],
            brief=database["farmData"]["Terminus Weapon"]["help"]
    )
    async def terminus_weapon(self,ctx):
        # Item to find
        item = "Terminus Weapon"
        await ctx.send(embed=self.getEmbed(item))

    @commands.command(
            aliases=["fortitude"],
            help=database["farmData"]["Fortitude Crystal"]["help"],
            brief=database["farmData"]["Fortitude Crystal"]["help"]
    )
    async def fortitude_crystal(self,ctx):
        # Item to find
        item = "Fortitude Crystal"
        await ctx.send(embed=self.getEmbed(item))

    @commands.command(
            aliases=["supplementary","sup"],
            help=database["farmData"]["Supplementary Damage"]["help"],
            brief=database["farmData"]["Supplementary Damage"]["help"]
    )
    async def supplementary_damage(self,ctx):
        # Item to find
        item = "Supplementary Damage"
        await ctx.send(embed=self.getEmbed(item))

    @commands.command(
            aliases=["war"],
            help=database["farmData"]["War Elemental"]["help"],
            brief=database["farmData"]["War Elemental"]["help"]
    )
    async def war_elemental(self,ctx):
        # Item to find
        item = "War Elemental"
        await ctx.send(embed=self.getEmbed(item))

    @commands.command(
            aliases=["curio"],
            help=database["farmData"]["Curios"]["help"],
            brief=database["farmData"]["Curios"]["help"]
    )
    async def curios(self,ctx):
        # Item to find
        item = "Curios"
        await ctx.send(embed=self.getEmbed(item))

class FAQ(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    def getEmbed(self, item):
        faq = database["faqData"]
        data = faq[item]
        display = data["data"]
        link = ""
        if "link" in data:
            link = data["link"]
        img = ""
        if "image" in data:
            img = data["image"]
        embed=discord.Embed(title=item, url=link, description=display, color=0xa0a0ff)
        embed.set_thumbnail(url=img)
        return embed

    @commands.command(
            aliases=["sigil"],
            help=database["faqData"]["Sigils"]["help"],
            brief=database["faqData"]["Sigils"]["help"]
    )
    async def sigil_farm(self, ctx):
        # Item to find
        item = "Sigils"
        await ctx.send(embed=self.getEmbed(item))
    
    @commands.command(
            help=database["faqData"]["AFK"]["help"],
            brief=database["faqData"]["AFK"]["help"]
    )
    async def afk(self, ctx):
        # Item to find
        item = "AFK"
        await ctx.send(embed=self.getEmbed(item))
    
    @commands.command(
            aliases=["calc","calculator"],
            help=database["faqData"]["Calculator"]["help"],
            brief=database["faqData"]["Calculator"]["help"]
    )
    async def damage_calculator(self, ctx):
        # Item to find
        item = "Calculator"
        await ctx.send(embed=self.getEmbed(item))
        
    @commands.command(
            aliases=["drop","drops","drop_rate"],
            help=database["faqData"]["Drops"]["help"],
            brief=database["faqData"]["Drops"]["help"]
    )
    async def drop_rate_table(self, ctx):
        # Item to find
        item = "Drops"
        await ctx.send(embed=self.getEmbed(item))

class Characters(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    def getEmbed(self, character, charType):
        chars = database["characters"]
        data = chars[character]
        charThread = data[charType]
        charColor = int(data["color"],0)
        img = ""
        if "image" in data:
            img = data["image"]
        embed=discord.Embed(title=character + " " + charType.capitalize(), url=charThread, description="Click [here]("+charThread+") to go to "+charType.capitalize(), color=charColor)
        embed.set_thumbnail(url=img)
        return embed

    @commands.command(
            help=database["characters"]["Narmaya"]["help"],
            brief=database["characters"]["Narmaya"]["help"]
    )
    async def narmaya(self, ctx):
        # Item to find
        character = "Narmaya"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["Io"]["help"],
            brief=database["characters"]["Io"]["help"]
    )
    async def io(self, ctx):
        # Item to find
        character = "Io"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))
