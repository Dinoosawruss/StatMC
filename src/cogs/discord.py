import discord
from discord.ext import commands


class Discord(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def discord(self, ctx):
        await ctx.send('Feel free to join our support discord at:\nhttps://discord.gg/2aEzQUe')


def setup(bot):
    bot.add_cog(Discord(bot))
