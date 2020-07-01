import discord
from discord.ext import commands

from func import options

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        embed=discord.Embed(title="About", url="https://dinoosawruss.github.io/NameBot-Site/", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
        embed.set_thumbnail(url=options.dinoLogo)
        embed.add_field(name="What is this?", value="This is an open source discord bot by @Dinoosawruss#5358 designed to make general queries about player's minecraft accounts such as their name history, hypixel stats, and, capes.", inline=False)
        embed.add_field(name="Acknowledgements", value="Name, skin, and, cape data by Mojang AB\nHypixel Stats Data by Hypixel\nSkin Renders by Crafatar.com\n5zig Cape Grabbing by 5zig Reborn\nLabyMod Cape Grabbing by LabyMod\nServer Info by MC-API", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(About(bot))
