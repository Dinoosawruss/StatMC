import discord
from discord.ext import commands

import requests
import base64
import os
from PIL import Image

from func import mojang, options

class LabyModCape(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["lmcape", "lcape", "labcape"])
    async def labycape(self, ctx, *, name):
        if len(name) <= 16:
            try:
                uuid = mojang.nameToDashUUID(name)
            
            except:
                await ctx.send(f"{ctx.author.mention} this username does not exist or could not be found...")
                pass

            url = f"https://www.labymod.net/page/php/getCapeTexture.php?uuid={uuid}"

            img_data = requests.get(url).content
            filename = f"{uuid}_labycape.png"
            with open(filename, 'wb') as handler:
                handler.write(img_data)
            
            #Image Cropping
            left = 1
            top = 1
            right = 11
            bottom = 16

            im = Image.open(filename)
            

            im1 = im.crop((left, top, right, bottom))
            im1.save(filename)
            im1 = im1.resize((40, 64), resample=Image.NEAREST)
            im1.save(filename)

            embed=discord.Embed(title="LabyMod Cape Lookup", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
            embed.set_thumbnail(url=options.labyLogo)
            embed.add_field(name="Current Username", value=f"{name}", inline=False)
            embed.add_field(name="UUID", value=f"{uuid}", inline=False)
            embed.add_field(name="Current LabyMod Cape", value=f"...", inline=False)

            await ctx.send(embed=embed)

            await ctx.send(file=discord.File(filename))

            os.remove(filename)


def setup(bot):
    bot.add_cog(LabyModCape(bot))
