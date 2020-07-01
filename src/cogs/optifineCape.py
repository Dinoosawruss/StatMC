import discord
from discord.ext import commands

import os
import wget
import requests
from PIL import Image

from func import mojang, options, lbFunc

class OptiFineCape(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def opticape(self, ctx, *, name):
        try:
            uuid = mojang.nameToUUID(name)
        
        except:
            await ctx.send(f"{ctx.author.mention} this username does not exist or could not be found...")
            return
        
        #Image Cropping
        left = 2
        top = 2
        right = 22
        bottom = 34
        
        try:
            im = wget.download(f"http://s.optifine.net/capes/{name}.png")
        except:
            await ctx.send(f"{ctx.author.mention} this user does not own an OptiFine cape...")
            return

        im = Image.open(f"{name}.png")
        

        im1 = im.crop((left, top, right, bottom))
        im1.save(f"{name}.png")
        im1 = im1.resize((40, 64), resample=Image.NEAREST)
        im1.save(f"{name}.png")

        embed=discord.Embed(title="OptiFine Cape Lookup", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
        embed.set_thumbnail(url=options.optifineLogo)
        embed.add_field(name="Current Username", value=f"{name}", inline=False)
        embed.add_field(name="UUID", value=f"{uuid}", inline=False)
        embed.add_field(name="Current OptiFine Cape", value=f"...", inline=False)
        await ctx.send(embed=embed)

        await ctx.send(file=discord.File(f"{name}.png"))

        os.remove(f"{name}.png")

        lbFunc.add(name)


def setup(bot):
    bot.add_cog(OptiFineCape(bot))
