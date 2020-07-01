import discord
from discord.ext import commands

from func import serverFunc, options

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def server(self, ctx, ip):
        server = serverFunc.getServerStatus(ip)

        embed=discord.Embed(title="Server Info Lookup", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
        embed.set_thumbnail(url=server['favicon'])
        embed.add_field(name="IP", value=server['ip'], inline=False)
        embed.add_field(name="MOTD", value=f"`{server['desc']}`", inline=False)
        embed.add_field(name="Online Players", value=f"{server['onlinePlayers']}/{server['maxPlayers']}", inline=True)
        embed.add_field(name="Capacity", value=f"{round((server['onlinePlayers']/server['maxPlayers'])*100, 2)}%", inline=True)
        embed.add_field(name="Version", value=server['version'], inline=False)
        embed.add_field(name="Protocol", value=server['protocol'], inline=False)
        
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Server(bot))
