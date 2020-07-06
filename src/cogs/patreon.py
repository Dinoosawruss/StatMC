import discord
from discord.ext import commands


class Patreon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def patreon(self, ctx):
        await ctx.send('If you\'d like to support us and become a patreon, please consider doing so at:\n<https://www.patreon.com/statmc>')


def setup(bot):
    bot.add_cog(Patreon(bot))
