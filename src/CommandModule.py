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
        faq = database["farmdata"]
        data = faq[item]
        name = data["title"]
        display = data["data"]
        link = ""
        if "link" in data:
            link = data["link"]
        img = ""
        if "image" in data:
            img = data["image"]
        embed=discord.Embed(title=name, url=link, description=display, color=0xa0a0ff)
        embed.set_thumbnail(url=img)
        return embed

    @commands.command(
            aliases=["terminus"],
            help=database["farmdata"]["terminusweapon"]["help"],
            brief=database["farmdata"]["terminusweapon"]["help"]
    )
    async def terminus_weapon(self,ctx):
        # Item to find
        item = "terminusweapon"
        await ctx.send(embed=self.getEmbed(item))

    @commands.command(
            aliases=["fortitude","fortitudecrystal","crystal"],
            help=database["farmdata"]["fortitudecrystal"]["help"],
            brief=database["farmdata"]["fortitudecrystal"]["help"]
    )
    async def fortitude_crystal(self,ctx):
        # Item to find
        item = "fortitudecrystal"
        await ctx.send(embed=self.getEmbed(item))

    @commands.command(
            aliases=["supplementarydamage","supplementary","sup"],
            help=database["farmdata"]["supplementarydamage"]["help"],
            brief=database["farmdata"]["supplementarydamage"]["help"]
    )
    async def supplementary_damage(self,ctx):
        # Item to find
        item = "supplementarydamage"
        await ctx.send(embed=self.getEmbed(item))

    @commands.command(
            aliases=["warelemental","war"],
            help=database["farmdata"]["warelemental"]["help"],
            brief=database["farmdata"]["warelemental"]["help"]
    )
    async def war_elemental(self,ctx):
        # Item to find
        item = "warelemental"
        await ctx.send(embed=self.getEmbed(item))

    @commands.command(
            aliases=["curio"],
            help=database["farmdata"]["curios"]["help"],
            brief=database["farmdata"]["curios"]["help"]
    )
    async def curios(self,ctx):
        # Item to find
        item = "curios"
        await ctx.send(embed=self.getEmbed(item))

    @commands.command(
        aliases=["weaponmaterials","weaponmats","wepmats"],
        help=database["farmdata"]["weaponmaterials"]["help"],
        brief=database["farmdata"]["weaponmaterials"]["help"]
    )
    async def weapon_materials(self, ctx):
        # Item to find
        item = "weaponmaterials"
        await ctx.send(embed=self.getEmbed(item))

class FAQ(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    def getEmbed(self, item):
        faq = database["faqdata"]
        data = faq[item]
        name = data["title"]
        display = data["data"]
        link = ""
        if "link" in data:
            link = data["link"]
        img = ""
        if "image" in data:
            img = data["image"]
        embed=discord.Embed(title=name, url=link, description=display, color=0xa0a0ff)
        embed.set_thumbnail(url=img)
        return embed

    @commands.command(
            aliases=["sigildroptable","sigil_drop","sigildrop"],
            help=database["faqdata"]["sigildrops"]["help"],
            brief=database["faqdata"]["sigildrops"]["help"]
    )
    async def sigil_drop_table(self, ctx):
        # Item to find
        item = "sigildrops"
        await ctx.send(embed=self.getEmbed(item))
    
    @commands.command(
            help=database["faqdata"]["afk"]["help"],
            brief=database["faqdata"]["afk"]["help"]
    )
    async def afk(self, ctx):
        # Item to find
        item = "afk"
        await ctx.send(embed=self.getEmbed(item))
    
    @commands.command(
            aliases=["damagecalculator","calculator","calc"],
            help=database["faqdata"]["calculator"]["help"],
            brief=database["faqdata"]["calculator"]["help"]
    )
    async def damage_calculator(self, ctx):
        # Item to find
        item = "calculator"
        await ctx.send(embed=self.getEmbed(item))
        
    @commands.command(
            aliases=["questratetabe","questrate","quest_rate","questdrops","quest_drops"],
            help=database["faqdata"]["questdrops"]["help"],
            brief=database["faqdata"]["questdrops"]["help"]
    )
    async def quest_rate_table(self, ctx):
        # Item to find
        item = "questdrops"
        await ctx.send(embed=self.getEmbed(item))
    

    @commands.command(
            aliases=["curiodroptable","curio_drop","curiodrop"],
            help=database["faqdata"]["curiodrops"]["help"],
            brief=database["faqdata"]["curiodrops"]["help"]
    )
    async def curio_drop_table(self, ctx):
        # Item to find
        item = "curiodrops"
        await ctx.send(embed=self.getEmbed(item))

    
    @commands.command(
            aliases=["dpsmeter","dps"],
            help=database["faqdata"]["dpsmeter"]["help"],
            brief=database["faqdata"]["dpsmeter"]["help"]
    )
    async def dps_meter(self, ctx):
        # Item to find
        item = "dpsmeter"
        await ctx.send(embed=self.getEmbed(item))

    @commands.command(
            aliases=["skillissue"],
            help=database["faqdata"]["skillissue"]["help"],
            brief=database["faqdata"]["skillissue"]["help"]
    )
    async def skill_issue(self, ctx):
        # Item to find
        item = "skillissue"
        await ctx.send(embed=self.getEmbed(item))
    
    @commands.command(
            aliases=["damagecap","dmgcap","cap"],
            help=database["faqdata"]["damagecap"]["help"],
            brief=database["faqdata"]["damagecap"]["help"]
    )
    async def damage_cap(self, ctx):
        # Item to find
        item = "damagecap"
        await ctx.send(embed=self.getEmbed(item))
    
    @commands.command(
            aliases=["pin"],
            help=database["faqdata"]["pins"]["help"],
            brief=database["faqdata"]["pins"]["help"]
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
        embed=discord.Embed(title=character.capitalize() + " " + charType.capitalize(), url=charThread, description=charDescription, color=charColor)
        if "image" in data:
            embed.set_thumbnail(url=data["image"])
        return embed

    @commands.command(
            help=database["characters"]["narmaya"]["help"],
            brief=database["characters"]["narmaya"]["help"]
    )
    async def narmaya(self, ctx):
        # Item to find
        character = "narmaya"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["io"]["help"],
            brief=database["characters"]["io"]["help"]
    )
    async def io(self, ctx):
        # Item to find
        character = "io"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))
    
    @commands.command(
            aliases=["gran","djeeta"],
            help=database["characters"]["captain"]["help"],
            brief=database["characters"]["captain"]["help"]
    )
    async def captain(self, ctx):
        # Item to find
        character = "captain"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))
    
    @commands.command(
            help=database["characters"]["katalina"]["help"],
            brief=database["characters"]["katalina"]["help"]
    )
    async def katalina(self, ctx):
        # Item to find
        character = "katalina"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))
    
    @commands.command(
            help=database["characters"]["rackam"]["help"],
            brief=database["characters"]["rackam"]["help"]
    )
    async def rackam(self, ctx):
        # Item to find
        character = "rackam"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))
    
    @commands.command(
            help=database["characters"]["eugen"]["help"],
            brief=database["characters"]["eugen"]["help"]
    )
    async def eugen(self, ctx):
        # Item to find
        character = "eugen"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))
    
    @commands.command(
            help=database["characters"]["rosetta"]["help"],
            brief=database["characters"]["rosetta"]["help"]
    )
    async def rosetta(self, ctx):
        # Item to find
        character = "rosetta"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["ferry"]["help"],
            brief=database["characters"]["ferry"]["help"]
    )
    async def ferry(self, ctx):
        # Item to find
        character = "ferry"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))
    
    @commands.command(
            help=database["characters"]["lancelot"]["help"],
            brief=database["characters"]["lancelot"]["help"]
    )
    async def lancelot(self, ctx):
        # Item to find
        character = "lancelot"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))
    
    @commands.command(
            help=database["characters"]["percival"]["help"],
            brief=database["characters"]["percival"]["help"]
    )
    async def percival(self, ctx):
        # Item to find
        character = "percival"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["vane"]["help"],
            brief=database["characters"]["vane"]["help"]
    )
    async def vane(self, ctx):
        # Item to find
        character = "vane"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["siegfried"]["help"],
            brief=database["characters"]["siegfried"]["help"]
    )
    async def siegfried(self, ctx):
        # Item to find
        character = "siegfried"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["charlotta"]["help"],
            brief=database["characters"]["charlotta"]["help"]
    )
    async def charlotta(self, ctx):
        # Item to find
        character = "charlotta"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["yodarha"]["help"],
            brief=database["characters"]["yodarha"]["help"]
    )
    async def yodarha(self, ctx):
        # Item to find
        character = "yodarha"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["zeta"]["help"],
            brief=database["characters"]["zeta"]["help"]
    )
    async def zeta(self, ctx):
        # Item to find
        character = "zeta"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["vaseraga"]["help"],
            brief=database["characters"]["vaseraga"]["help"]
    )
    async def vaseraga(self, ctx):
        # Item to find
        character = "vaseraga"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["cagliostro"]["help"],
            brief=database["characters"]["cagliostro"]["help"]
    )
    async def cagliostro(self, ctx):
        # Item to find
        character = "cagliostro"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["ghandagoza"]["help"],
            brief=database["characters"]["ghandagoza"]["help"]
    )
    async def ghandagoza(self, ctx):
        # Item to find
        character = "ghandagoza"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

    @commands.command(
            help=database["characters"]["id"]["help"],
            brief=database["characters"]["id"]["help"]
    )
    async def id(self, ctx):
        # Item to find
        character = "id"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"thread"))

class CharBuild(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    def getBuild(self, character, charType):
        charData = database["charbuild"][character][charType]
        charColor = int(database["characters"][character]["color"],0)
        embed=discord.Embed(title=charData["title"], description=charData["notes"], color=charColor)
        if "image" in database["characters"][character]:
            embed.set_thumbnail(url=database["characters"][character]["image"])
        embed.set_image(url=charData["link"])
        return embed


    @commands.command(
            help=database["charbuild"]["help"],
            brief=database["charbuild"]["help"]
    )
    async def build(self, ctx):
        msgSplit = ctx.message.content.split()
        if len(msgSplit) > 1:
            character = msgSplit[1].lower()
            if character not in database["charbuild"].keys():
                await ctx.send(character + " is not supported.")
                return

            if len(msgSplit) > 2:
                charType = msgSplit[2]
                if charType in database["charbuild"][character]:
                    await ctx.send(embed=self.getBuild(character,charType))
                    return

            output = "```" + character.capitalize() + " Builds:\n"
            for item in database["charbuild"][character]:
                if item.isnumeric():
                    output += item + ": " + database["charbuild"][character][item]["title"] + " \n"
            output += "Please input a number to pick your build```"
            await ctx.send(output)
            return

        output = "```\n"
        for item in database["charbuild"]:
            if item == "help":
                continue
            output += item.capitalize() + "\n"
        output += "Please input a character to pick your build```"
        await ctx.send(output)

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