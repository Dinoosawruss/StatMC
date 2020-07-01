import discord
from discord.ext import commands


class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        """
        A test command, Mainly used to show how commands and cogs should be laid out.
        """
        await ctx.send(f'{ctx.author.mention} you can invite the bot with the following link:\n')


def setup(bot):
    bot.add_cog(Invite(bot))
