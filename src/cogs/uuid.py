import discord
from discord.ext import commands

from func import mojang, options, lbFunc

class UUID(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uuid(self, ctx, *, name):
        try:
            uuid = mojang.nameToUUID(name)

        except:
            await ctx.send(f"{ctx.author.mention} this username does not exist or could not be found...")
            return

        await ctx.send(f"{ctx.author.mention} {name}'s uuid is:\n`{uuid}`")    

        lbFunc.add(name)

    @commands.command()
    async def dashuuid(self, ctx, *, name):
        try:
            uuid = mojang.nameToDashUUID(name)

        except:
            await ctx.send(f"{ctx.author.mention} this username does not exist or could not be found...")
            return

        await ctx.send(f"{ctx.author.mention} {name}'s uuid is:\n`{uuid}`")    

        lbFunc.add(name)
    


def setup(bot):
    bot.add_cog(UUID(bot))
