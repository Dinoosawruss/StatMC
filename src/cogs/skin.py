import discord
from discord.ext import commands

from func import mojang, options, lbFunc

class Skin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def skin(self, ctx, *, name):
        if len(name) <= 16:
            try:
                uuid = mojang.nameToUUID(name)
            
            except:
                await ctx.send(f"{ctx.author.mention} this username does not exist or could not be found...")
                return

        embed = discord.Embed()
        embed=discord.Embed(title="Skin Lookup", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
        embed.set_thumbnail(url=options.mojangLogo)
        embed.add_field(name="Current Username", value=f"{name}", inline=False)
        embed.add_field(name="UUID", value=f"{uuid}", inline=False)
        embed.add_field(name="Current Skin", value="...", inline=False)
        embed.set_image(url=f"https://crafatar.com/renders/body/{uuid}.png")
        await ctx.send(embed=embed)

        lbFunc.add(name)

    @commands.command()
    async def skinfile(self, ctx, *, name):
        if len(name) <= 16:
            try:
                uuid = mojang.nameToUUID(name)
            
            except:
                await ctx.send(f"{ctx.author.mention} this username does not exist or could not be found...")
                return
            
            embed = discord.Embed()
            embed=discord.Embed(title="Skin Lookup", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
            embed.set_thumbnail(url=options.mojangLogo)
            embed.add_field(name="Current Username", value=f"{name}", inline=False)
            embed.add_field(name="UUID", value=f"{uuid}", inline=False)
            embed.add_field(name="Raw Skin File", value="...", inline=False)
            embed.set_image(url=f"https://crafatar.com/skins/{uuid}.png")
            await ctx.send(embed=embed)

            lbFunc.add(name)


def setup(bot):
    bot.add_cog(Skin(bot))
