import discord
from discord import app_commands
from discord.ext import commands
from typing import List
import os, json

# Setup global database
global dataFile, database
cwd = os.path.dirname(os.path.realpath(__file__))
dataFile = open(cwd + "/../Database.json")
database = json.load(dataFile)

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
    
    async def char_autocomplete(self, interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
        chars = list(database["characters"].keys())
        return [
            app_commands.Choice(name=char.capitalize(), value=char)
            for char in chars if current.lower() in char.lower()
        ][:25]
        
    # Slash Command : /guide
    @app_commands.command(
        name="guide",
        description="This command will provide some of the community guide for specified character."
    )
    @app_commands.describe(
        character="The character of your choice"
    )
    @app_commands.autocomplete(
        character=char_autocomplete
    )
    async def get_character(self, interaction: discord.Interaction, character: str):
        if character not in database["characters"].keys():
            await interaction.response.send_message(content=f"{character} is not supported.")
            return
        await interaction.response.send_message(embeds=[self.getEmbed(character, "guide"), self.getEmbed(character, "channel")])
        return


    # Context Command
    @commands.command(
            help=database["characters"]["narmaya"]["help"],
            brief=database["characters"]["narmaya"]["help"]
    )
    async def narmaya(self, ctx):
        # Item to find
        character = "narmaya"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))

    @commands.command(
            help=database["characters"]["io"]["help"],
            brief=database["characters"]["io"]["help"]
    )
    async def io(self, ctx):
        # Item to find
        character = "io"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))
    
    @commands.command(
            aliases=["gran","djeeta"],
            help=database["characters"]["captain"]["help"],
            brief=database["characters"]["captain"]["help"]
    )
    async def captain(self, ctx):
        # Item to find
        character = "captain"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))
    
    @commands.command(
            help=database["characters"]["katalina"]["help"],
            brief=database["characters"]["katalina"]["help"]
    )
    async def katalina(self, ctx):
        # Item to find
        character = "katalina"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))
    
    @commands.command(
            help=database["characters"]["rackam"]["help"],
            brief=database["characters"]["rackam"]["help"]
    )
    async def rackam(self, ctx):
        # Item to find
        character = "rackam"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))
    
    @commands.command(
            help=database["characters"]["eugen"]["help"],
            brief=database["characters"]["eugen"]["help"]
    )
    async def eugen(self, ctx):
        # Item to find
        character = "eugen"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))
    
    @commands.command(
            help=database["characters"]["rosetta"]["help"],
            brief=database["characters"]["rosetta"]["help"]
    )
    async def rosetta(self, ctx):
        # Item to find
        character = "rosetta"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))

    @commands.command(
            help=database["characters"]["ferry"]["help"],
            brief=database["characters"]["ferry"]["help"]
    )
    async def ferry(self, ctx):
        # Item to find
        character = "ferry"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))
    
    @commands.command(
            help=database["characters"]["lancelot"]["help"],
            brief=database["characters"]["lancelot"]["help"]
    )
    async def lancelot(self, ctx):
        # Item to find
        character = "lancelot"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))
    
    @commands.command(
            help=database["characters"]["percival"]["help"],
            brief=database["characters"]["percival"]["help"]
    )
    async def percival(self, ctx):
        # Item to find
        character = "percival"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))

    @commands.command(
            help=database["characters"]["vane"]["help"],
            brief=database["characters"]["vane"]["help"]
    )
    async def vane(self, ctx):
        # Item to find
        character = "vane"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))

    @commands.command(
            help=database["characters"]["siegfried"]["help"],
            brief=database["characters"]["siegfried"]["help"]
    )
    async def siegfried(self, ctx):
        # Item to find
        character = "siegfried"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))

    @commands.command(
            help=database["characters"]["charlotta"]["help"],
            brief=database["characters"]["charlotta"]["help"]
    )
    async def charlotta(self, ctx):
        # Item to find
        character = "charlotta"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))

    @commands.command(
            help=database["characters"]["yodarha"]["help"],
            brief=database["characters"]["yodarha"]["help"]
    )
    async def yodarha(self, ctx):
        # Item to find
        character = "yodarha"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))

    @commands.command(
            help=database["characters"]["zeta"]["help"],
            brief=database["characters"]["zeta"]["help"]
    )
    async def zeta(self, ctx):
        # Item to find
        character = "zeta"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))

    @commands.command(
            help=database["characters"]["vaseraga"]["help"],
            brief=database["characters"]["vaseraga"]["help"]
    )
    async def vaseraga(self, ctx):
        # Item to find
        character = "vaseraga"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))

    @commands.command(
            help=database["characters"]["cagliostro"]["help"],
            brief=database["characters"]["cagliostro"]["help"]
    )
    async def cagliostro(self, ctx):
        # Item to find
        character = "cagliostro"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))

    @commands.command(
            help=database["characters"]["ghandagoza"]["help"],
            brief=database["characters"]["ghandagoza"]["help"]
    )
    async def ghandagoza(self, ctx):
        # Item to find
        character = "ghandagoza"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))

    @commands.command(
            help=database["characters"]["id"]["help"],
            brief=database["characters"]["id"]["help"]
    )
    async def id(self, ctx):
        # Item to find
        character = "id"
        await ctx.send(embed=self.getEmbed(character,"guide"))
        await ctx.send(embed=self.getEmbed(character,"channel"))

async def setup(client):
    await client.add_cog(Characters(client))