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
    
    async def topic_autocomplete(self, interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
        faq_data = list(database["faqdata"].keys())
        options = []
        
        for data in faq_data:
            name = database["faqdata"][data]["title"]
            if (current.lower() in name.lower()):
                options.append(app_commands.Choice(name=name.capitalize(), value=data))
        
        return options[:25]
    
    # Slash Command : /faq
    @app_commands.command(
        name="faq",
        description="This command will provide some of the FAQ you might want to know."
    )
    @app_commands.describe(
        topic="The topic of your choice"
    )
    @app_commands.autocomplete(
        topic=topic_autocomplete
    )
    async def get_faq(self, interaction: discord.Interaction, topic: str):
        if topic not in database["faqdata"].keys():
            await interaction.response.send_message(content=f"{topic} is not supported.")
            return
        await interaction.response.send_message(embeds=[self.getEmbed(topic)])
        return

    # Context command
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
            aliases=["damagecalculator","calculator","calc","damagecalc","dmgcalc"],
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
            help=database["faqdata"]["awakening"]["help"],
            brief=database["faqdata"]["awakening"]["help"]
    )
    async def awakening(self, ctx):
        # Item to find
        item = "awakening"
        await ctx.send(embed=self.getEmbed(item))
    
    @commands.command(
            aliases=["pin"],
            help=database["faqdata"]["pins"]["help"],
            brief=database["faqdata"]["pins"]["help"]
    )
    async def pins(self, ctx):
        # Item to find
        await ctx.send("Read the Pins")

async def setup(client):
    await client.add_cog(FAQ(client))