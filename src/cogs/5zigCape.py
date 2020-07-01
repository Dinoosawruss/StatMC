import discord
from discord.ext import commands

import requests
import base64
import os
import json
from PIL import Image

from func import mojang, options

class ZigCape(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["5zigcape", "zcape"])
    async def zigcape(self, ctx, *, name):
        if len(name) <= 16:
            try:
                uuid = mojang.nameToDashUUID(name)
            
            except:
                await ctx.send(f"{ctx.author.mention} this username does not exist or could not be found...")
                pass

            print(uuid)
            data = requests.get(f"https://textures.5zigreborn.eu/profile/{uuid}").json()

            if data['d'] is None:
                await ctx.send(f"{ctx.author.mention} this user does not own a 5zig cape...")
                return
    
            
            imgdata = base64.b64decode(data['d'])
            filename = f'{uuid}_cape.png'  
            with open(filename, 'wb') as f:
                f.write(imgdata)

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

            embed=discord.Embed(title="5zig Cape Lookup", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
            embed.set_thumbnail(url=options.zigLogo)
            embed.add_field(name="Current Username", value=f"{name}", inline=False)
            embed.add_field(name="UUID", value=f"{uuid}", inline=False)
            embed.add_field(name="Current 5zig Cape", value=f"...", inline=False)
            
            await ctx.send(embed=embed)

            await ctx.send(file=discord.File(filename))

            os.remove(filename)


def setup(bot):
    bot.add_cog(ZigCape(bot))
