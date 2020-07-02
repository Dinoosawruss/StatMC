import discord
from discord.ext import commands


class Skyblock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def skyblock(self, ctx):
        await ctx.send('This command is still being worked on')


def setup(bot):
    bot.add_cog(Skyblock(bot))
