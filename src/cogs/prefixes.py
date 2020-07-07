import discord
from discord.ext import commands
import os
import json


class Prefixes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, prefix):
        """
        Changes the server prefix for the bot!
        """
        with open('data/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('data/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)
        await ctx.send(f"The prefix for this guild is now {prefix}.")
        


def setup(bot):
    bot.add_cog(Prefixes(bot))
