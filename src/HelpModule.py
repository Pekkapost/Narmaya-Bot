import discord
from discord.ext import commands

class MyHelpCommand(commands.DefaultHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(title="WIP Menu",color=discord.Color.blurple(), description="")

        for page in self.paginator.pages:
            e.description += page

        await destination.send(embed=e)