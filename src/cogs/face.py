import discord
from discord.ext import commands

from func import mojang, options, lbFunc

class Face(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def face(self, ctx, *, name):
        if len(name) <= 16:
            try:
                uuid = mojang.nameToUUID(name)

            except:
                await ctx.send(f"{ctx.author.mention} this username does not exist or could not be found...")
                return
            
            embed = discord.Embed()
            embed=discord.Embed(title="Skin Lookup", description=f"The results {ctx.author}'s lookup", color=options.getEmbedColour(ctx.guild.id))
            embed.set_thumbnail(url=options.mojangLogo)
            embed.add_field(name="Current Username", value=f"{name}", inline=False)
            embed.add_field(name="UUID", value=f"{uuid}", inline=False)
            embed.add_field(name="Raw Skin File", value="...", inline=False)
            embed.set_image(url=f"https://crafatar.com/avatars/{uuid}.png")
            await ctx.send(embed=embed)
            
        lbFunc.add(name)

def setup(bot):
    bot.add_cog(Face(bot))
