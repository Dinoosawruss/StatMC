import discord
from discord.ext import commands


class Guilds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guilds(self, ctx):
        await ctx.send(f'I am currently in {len(self.bot.guilds)} guilds.')


def setup(bot):
    bot.add_cog(Guilds(bot))
