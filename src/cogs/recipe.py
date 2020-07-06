import discord
from discord.ext import commands#

import json

from func import options

class Recipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def recipe(self, ctx, *, n=None):
        if n is None:
            await ctx.send(f'{ctx.author.mention} invalid syntax: `?recipe (item)`')

        else:
            with open('./data/recipes.json', 'r') as json_file:
                recipesFile = json.load(json_file)

            for recipe in recipesFile['recipe']:
                for name in recipe['names']:
                    if n.lower() == name or n.lower() == name + 's':
                        embed = discord.Embed(title="Recipe lookup", description=f"The result of {ctx.author}'s recipe lookup", color=options.getEmbedColour(ctx.guild.id))
                        embed.set_image(url=f"https://www.minecraftcrafting.info/imgs/craft_{recipe['url']}")

                        await ctx.send(embed=embed)
                        return

            await ctx.send(f"{ctx.author.mention} it appears we could not find the recipe you're looking for.\nI have informed the developers")
            
            recipesFile['unknown'].append(n)

            with open('./data/recipes.json', 'w') as json_file:
                json.dump(recipesFile, json_file, indent=2)


def setup(bot):
    bot.add_cog(Recipe(bot))
