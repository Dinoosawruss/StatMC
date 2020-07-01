import discord
from discord.ext import commands

from func import mojang, options, lbFunc

class MojangCape(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["mojangcape", "mcape"])
    async def mojcape(self, ctx, *, name):
        skipMojang = False
        if len(name) <= 16:
            try:
                uuid = mojang.nameToUUID(name)
            
            except:
                await ctx.send(f"{ctx.author.mention} this username does not exist or could not be found...")
                return

            
            capeLink = mojang.getMojangCape(uuid)

            if capeLink is None:
                await ctx.send(f"{ctx.author.mention} this user does not have a mojang cape...")
                skipMojang = True
                
            if not skipMojang:
                for cape in mojang.capes:
                    if capeLink['url'] == f"http://textures.minecraft.net/texture/{cape['url']}":
                        embed=discord.Embed(title="Cape Lookup", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
                        embed.set_thumbnail(url=options.mojangLogo)
                        embed.add_field(name="Current Username", value=f"{name}", inline=False)
                        embed.add_field(name="UUID", value=f"{uuid}", inline=False)
                        embed.add_field(name="Current Cape", value=f"{cape['name']}", inline=False)
                        await ctx.send(embed=embed)

                        await ctx.send(file=discord.File(f"./capes/{cape['image']}"))

                lbFunc.add(name)


def setup(bot):
    bot.add_cog(MojangCape(bot))
