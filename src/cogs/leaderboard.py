import discord
from discord.ext import commands

from func import mojang, options, lbFunc

class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def leaderboard(self, ctx):
        lb = lbFunc.getTop()
        embed = discord.Embed()
        embed=discord.Embed(title="Leaderboard", description=f"Top searched players", color=options.getEmbedColour(ctx.guild.id))

        x = 0
        for player in lb:
            x += 1
            embed.add_field(name=f"#{x}:", value=f"{player[1]} - {player[0]} queries", inline=False)
            if x == 10:
                break

        await ctx.send(embed=embed)

    @commands.command()
    async def purgeleaderboard(self, ctx, *, reason):
        if ctx.author.id == 221957178217463808:
            lbFunc.purge(reason, ctx.author)

def setup(bot):
    bot.add_cog(Leaderboard(bot))
