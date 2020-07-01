import discord
from discord.ext import commands

import wget
import requests
import json
import os
from PIL import Image
from func import mojang, options, lbFunc

class Cape(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cape(self, ctx, *, name):
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
                
                    
            #print(capeLink['url'])
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
            im1 = im1.resize((40, 64))
            im1.save(f"{name}.png")

            embed=discord.Embed(title="OptiFine Cape Lookup", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
            embed.set_thumbnail(url=options.mojangLogo)
            embed.add_field(name="Current Username", value=f"{name}", inline=False)
            embed.add_field(name="UUID", value=f"{uuid}", inline=False)
            embed.add_field(name="Current OptiFine Cape", value=f"...", inline=False)
            await ctx.send(embed=embed)

            await ctx.send(file=discord.File(f"{name}.png"))

            os.remove(f"{name}.png")

        else:
            uuid = name
            capeLink = mojang.getMojangCape(uuid)

            await ctx.send(capeLink)

        lbFunc.add(name)


def setup(bot):
    bot.add_cog(Cape(bot))
