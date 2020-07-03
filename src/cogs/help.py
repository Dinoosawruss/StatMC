import discord
from discord.ext import commands

import json

from func import options

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *, query=None):
        embed=discord.Embed(title="Command List", description=f"The results {ctx.author}'s lookup", color=options.getEmbedColour(ctx.guild.id))
        embed.set_thumbnail(url=options.dinoLogo)
        
        with open("./data/commands.json", "r") as json_file:
            commands = json.load(json_file)

        if query is None:
            for key in commands:
                embed.add_field(name=f"?help {key.lower()}", value=commands[key][0]['desc'], inline=False)

            await ctx.send(embed=embed)

        else:
            for key in commands:
                if query.lower() == key.lower():
                    for i in range(1,len(commands[key])):
                        embed.add_field(name=commands[key][i]['command'], value=commands[key][i]['description'], inline=False)
                    
                    await ctx.send(embed=embed)
                    return
            
            await ctx.send(f"{ctx.author.mention} unknown help query...")
    


def setup(bot):
    bot.add_cog(Help(bot))
