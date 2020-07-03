import discord
from discord.ext import commands

from func import mojang, options, lbFunc

class History(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def history(self, ctx, *, name):
        try:
            if len(name) <= 16:
                uuid = mojang.nameToUUID(name)
                nameHistory = mojang.uuidToNameHistory(uuid)
                name = nameHistory[len(nameHistory)-1]

                previous = ""

                nameHistory.reverse()

                for uname in nameHistory:
                    previous += f"`{uname}`\n"

                embed=discord.Embed(title="Name History Lookup", description=f"The results {ctx.author}'s lookup", color=options.getEmbedColour(ctx.guild.id))
                embed.set_thumbnail(url=options.mojangLogo)
                embed.add_field(name="Current Username", value=f"{name}", inline=False)
                embed.add_field(name="UUID", value=f"{uuid}", inline=False)
                embed.add_field(name="Previous names", value=f"{previous}", inline=False)
                await ctx.send(embed=embed)

            else:
                nameHistory = mojang.uuidToNameHistory(name.replace("-", ""))
                uuid = name
                name = nameHistory[len(nameHistory)-1]
                
                previous = ""

                nameHistory.reverse()

                for uname in nameHistory:
                    previous += f"\n{uname}"

                embed=discord.Embed(title="Name History Lookup", description=f"The results {ctx.author}'s lookup", color=options.getEmbedColour(ctx.guild.id))
                embed.set_thumbnail(url=options.mojangLogo)
                embed.add_field(name="Current Username", value=f"{name}", inline=False)
                embed.add_field(name="UUID", value=f"{uuid}", inline=False)
                embed.add_field(name="Previous names", value=f"{previous}", inline=False)
                await ctx.send(embed=embed)

            lbFunc.add(name)

        except:
            await ctx.send(f"{ctx.author.mention} this username does not exist or could not be found...")



def setup(bot):
    bot.add_cog(History(bot))
