import discord
from discord.ext import commands

from func import mojang, options, lbFunc

from PIL import Image
import sys
import os

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

            
            capes = mojang.getMojangCape(name)
            
            images = []
            
            for x in capes:
                images.append(Image.open(f"./capes/{x[1]}"))

            print(images)
            widths, heights = zip(*(i.size for i in images))

            total_width = sum(widths)
            max_height = max(heights)

            new_im = Image.new('RGB', (total_width, max_height))

            x_offset = 0
            for im in images:
                new_im.paste(im, (x_offset,0))
                x_offset += im.size[0]

                new_im.save(f'{name}.png')
            
            

            capeText = ""
            
            for i in capes:
                capeText += f"{i[0]}\n"

            embed=discord.Embed(title="Cape Lookup", description=f"The results {ctx.author}'s lookup", color=options.getEmbedColour(ctx.guild.id))
            embed.set_thumbnail(url=options.mojangLogo)
            embed.add_field(name="Current Username", value=f"{name}", inline=False)
            embed.add_field(name="UUID", value=f"{uuid}", inline=False)
            embed.add_field(name="Current Capes", value=capeText, inline=False)
            await ctx.send(embed=embed)
            await ctx.send(file=discord.File(f"{name}.png"))

            os.remove(f"{name}.png")

def setup(bot):
    bot.add_cog(MojangCape(bot))
