from typing import Coroutine, List
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

# Select Menu Dropdown & View
class BuildDropdown(discord.ui.Select):
    def __init__(self, char, target):
        
        options = []
        builds = database["charbuild"][char].keys()
        
        for key in builds:
            build_name = database["charbuild"][char][key]["title"]
            options.append(discord.SelectOption(label=build_name, value=f"{char}_{key}", default=(key == target)))
        
        super().__init__(placeholder="Select one of the available build", options=options[:25])
        
    def getEmbed(self, character, charType):
        charData = database["charbuild"][character][charType]
        charColor = int(database["characters"][character]["color"],0)
        embed=discord.Embed(title=charData["title"], description=charData["notes"], color=charColor)
        if "image" in database["characters"][character]:
            embed.set_thumbnail(url=database["characters"][character]["image"])
        embed.set_image(url=charData["link"])
        return embed
        
    async def callback(self, interaction: discord.Interaction) -> None:
        char = self.values[0].split("_")[0]
        build = self.values[0].split("_")[1]
        
        for option in self.options:
            option.default = (option.value == f"{char}_{build}")
        
        await interaction.message.edit(embed=self.getEmbed(char, build), view=self.view)
        await interaction.response.defer()
        return
        
# Select Menu Dropdown is setup to timeout 60s from the latest interaction response
class DropdownView(discord.ui.View):
    def __init__(self, timeout=60):
        super().__init__(timeout=timeout)
    
    async def on_timeout(self):
        for item in self.children:
            item.disabled = True
            
        await self.message.edit(view=self)
        return


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
        embed.set_footer(text="*Select menu will be disabled in 60 seconds")
        return embed
    
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
        chars = list(database["charbuild"].keys())
        return [
            app_commands.Choice(name=char.capitalize(), value=char)
            for char in chars if (current.lower() in char.lower() and char.lower() != "help")
        ][:25]
        
    # Slash Command : /build
    @app_commands.command(
        name="build",
        description="This command will provide some of the sample build for specified character."
    )
    @app_commands.describe(
        character="The character of your choice"
    )
    @app_commands.autocomplete(
        character=char_autocomplete
    )
    async def get_character(self, interaction: discord.Interaction, character: str):
        await interaction.response.defer(thinking=True)
        
        if (character.lower() not in database["charbuild"].keys() or character.lower() == "help"):
            await interaction.followup.send(content=f"{character} is not supported.")
            return
                
        select_option = BuildDropdown(character, "1")
        select_view = DropdownView().add_item(select_option)
        select_view.message = await interaction.followup.send(embed=self.getBuild(character, "1"),view=select_view)
        return
    
    
    # Context command
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
            output += "Please use a number to pick your build\nEx: n!build narmaya 1```"
            await ctx.send(output)
            return

        output = "```\n"
        for item in database["charbuild"]:
            if item == "help":
                continue
            output += item.capitalize() + "\n"
        output += "Please use a character to display builds\nEx: n!build narmaya```"
        await ctx.send(output)

async def setup(client):
    await client.add_cog(CharBuild(client))