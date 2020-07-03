import discord
from discord.ext import commands

from func import mojang, options, lbFunc

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def profile(self, ctx, *, name):
        if len(name) <= 16:
            try:
                uuid = mojang.nameToUUID(name)

            except:
                await ctx.send(f"{ctx.author.mention} this username does not exist or could not be found...")
                return

            name = mojang.uuidToName(uuid)
            
            nameHistory = mojang.uuidToNameHistory(uuid)

            previous = ""

            nameHistory.reverse()

            for uname in nameHistory:
                previous += f"`{uname}`\n"

            embed = discord.Embed()
            embed=discord.Embed(title=f"{name}'s Profile'", description=f"The results {ctx.author}'s lookup", color=options.getEmbedColour(ctx.guild.id))
            embed.set_thumbnail(url=options.mojangLogo)
            embed.add_field(name="Current Username", value=name, inline=False)
            embed.add_field(name="UUID", value=uuid, inline=False)
            embed.add_field(name="Name History", value=f"{name} has changed their name {len(nameHistory)} times:\n{previous}", inline=False)
            embed.add_field(name="Current Skin", value="...", inline=False)
            embed.set_image(url=f"https://crafatar.com/renders/body/{uuid}.png")

            await ctx.send(embed=embed)
        
        
        return

def setup(bot):
    bot.add_cog(Profile(bot))

