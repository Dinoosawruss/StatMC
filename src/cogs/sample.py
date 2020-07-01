import discord
from discord.ext import commands


class Sample(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        """
        A test command, Mainly used to show how commands and cogs should be laid out.
        """
        await ctx.send('Tested!')


def setup(bot):
    bot.add_cog(Sample(bot))
