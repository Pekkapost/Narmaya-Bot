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
    
    @commands.command(
            aliases=["dps","dpsmeter"],
            help=database["faqData"]["DPSMeter"]["help"],
            brief=database["faqData"]["DPSMeter"]["help"]
    )
    async def dps_meter(self, ctx):
        # Item to find
        item = "DPSMeter"
        await ctx.send(embed=self.getEmbed(item))
    
    @commands.command(
            aliases=["pin"],
            help=database["faqData"]["Pins"]["help"],
            brief=database["faqData"]["Pins"]["help"]
    )
    async def pins(self, ctx):
        # Item to find
        await ctx.send("Read the Pins")

class Characters(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    def getEmbed(self, character, charType):
        chars = database["characters"]
        data = chars[character]
        charThread = data[charType]
        if charThread == "":
            charDescription = "No guide exists"
        else:
            charDescription = "Click [here]("+charThread+") to go to "+charType.capitalize()
        charColor = int(data["color"],0)
        embed=discord.Embed(title=character + " " + charType.capitalize(), url=charThread, description=charDescription, color=charColor)
        if "image" in data:
            embed.set_thumbnail(url=data["image"])
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
    
    @commands.command(
            aliases=["gran","djeeta"],
            help=database["characters"]["Captain"]["help"],
            brief=database["characters"]["Captain"]["help"]
    )
    async def captain(self, ctx):
        # Item to find
        character = "Captain"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))
    
    @commands.command(
            help=database["characters"]["Katalina"]["help"],
            brief=database["characters"]["Katalina"]["help"]
    )
    async def katalina(self, ctx):
        # Item to find
        character = "Katalina"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))
    
    @commands.command(
            help=database["characters"]["Rackam"]["help"],
            brief=database["characters"]["Rackam"]["help"]
    )
    async def rackam(self, ctx):
        # Item to find
        character = "Rackam"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))
    
    @commands.command(
            help=database["characters"]["Eugen"]["help"],
            brief=database["characters"]["Eugen"]["help"]
    )
    async def eugen(self, ctx):
        # Item to find
        character = "Eugen"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))
    
    @commands.command(
            help=database["characters"]["Rosetta"]["help"],
            brief=database["characters"]["Rosetta"]["help"]
    )
    async def rosetta(self, ctx):
        # Item to find
        character = "Rosetta"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["Ferry"]["help"],
            brief=database["characters"]["Ferry"]["help"]
    )
    async def ferry(self, ctx):
        # Item to find
        character = "Ferry"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))
    
    @commands.command(
            help=database["characters"]["Lancelot"]["help"],
            brief=database["characters"]["Lancelot"]["help"]
    )
    async def lancelot(self, ctx):
        # Item to find
        character = "Lancelot"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))
    
    @commands.command(
            help=database["characters"]["Percival"]["help"],
            brief=database["characters"]["Percival"]["help"]
    )
    async def percival(self, ctx):
        # Item to find
        character = "Percival"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["Vane"]["help"],
            brief=database["characters"]["Vane"]["help"]
    )
    async def vane(self, ctx):
        # Item to find
        character = "Vane"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["Siegfried"]["help"],
            brief=database["characters"]["Siegfried"]["help"]
    )
    async def siegfried(self, ctx):
        # Item to find
        character = "Siegfried"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["Charlotta"]["help"],
            brief=database["characters"]["Charlotta"]["help"]
    )
    async def charlotta(self, ctx):
        # Item to find
        character = "Charlotta"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["Yodarha"]["help"],
            brief=database["characters"]["Yodarha"]["help"]
    )
    async def yodarha(self, ctx):
        # Item to find
        character = "Yodarha"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["Zeta"]["help"],
            brief=database["characters"]["Zeta"]["help"]
    )
    async def zeta(self, ctx):
        # Item to find
        character = "Zeta"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["Vaseraga"]["help"],
            brief=database["characters"]["Vaseraga"]["help"]
    )
    async def vaseraga(self, ctx):
        # Item to find
        character = "Vaseraga"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["Cagliostro"]["help"],
            brief=database["characters"]["Cagliostro"]["help"]
    )
    async def cagliostro(self, ctx):
        # Item to find
        character = "Cagliostro"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["Ghandagoza"]["help"],
            brief=database["characters"]["Ghandagoza"]["help"]
    )
    async def ghandagoza(self, ctx):
        # Item to find
        character = "Ghandagoza"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["Id"]["help"],
            brief=database["characters"]["Id"]["help"]
    )
    async def id(self, ctx):
        # Item to find
        character = "Id"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

class CharBuild(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    def getBuild(self, character, charType):
        charData = database["charBuild"]["Narmaya"][charType]
        charColor = int(database["characters"][character]["color"],0)
        embed=discord.Embed(title=charData["title"], description=charData["notes"], color=charColor)
        embed.set_image(url=charData["link"])
        return embed


    @commands.command(
            alias=["narmbuild"],
            help=database["charBuild"]["Narmaya"]["help"],
            brief=database["charBuild"]["Narmaya"]["help"]
    )
    async def narmayabuild(self, ctx):
        character = "Narmaya"
        msgSplit = ctx.message.content.split()
        if len(msgSplit) > 1:
            charType = msgSplit[1]
            if charType not in database["charBuild"][character]:
                return
            await ctx.send(embed=self.getBuild(character,charType))
        else:
            output = "```"
            for item in database["charBuild"]["Narmaya"]:
                if item.isnumeric():
                    output += item + ": " + database["charBuild"]["Narmaya"][item]["title"] + " \n"
            output += "Please input a number to pick your build```"
            await ctx.send(output)

