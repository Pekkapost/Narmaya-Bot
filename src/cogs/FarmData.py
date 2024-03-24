from typing import List
import discord
from discord import app_commands
from discord.ext import commands
import json
import os
import re

global dataFile, database
cwd = os.path.dirname(os.path.realpath(__file__))
dataFile = open(cwd + "/../Database.json")
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

    async def item_autocomplete(self, interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
        faq_data = list(database["farmdata"].keys())
        options = []
        
        for data in faq_data:
            name = database["farmdata"][data]["title"]
            if (current.lower() in name.lower()):
                options.append(app_commands.Choice(name=name.capitalize(), value=data))
        
        return options[:25]
    
    # Slash Command : /farm
    @app_commands.command(
        name="farm",
        description="This command will provide some of the best farm place for items."
    )
    @app_commands.describe(
        item="The item of your choice"
    )
    @app_commands.autocomplete(
        item=item_autocomplete
    )
    async def get_faq(self, interaction: discord.Interaction, item: str):
        if item not in database["farmdata"].keys():
            await interaction.response.send_message(content=f"{item} is not supported.")
            return
        await interaction.response.send_message(embeds=[self.getEmbed(item)])
        return

    # Context Command
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
        
async def setup(client):
    await client.add_cog(FarmData(client))