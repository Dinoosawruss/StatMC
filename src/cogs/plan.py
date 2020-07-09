import discord
from discord.ext import commands

from modules import player
from func import options

import sqlite3
import json
import os

class Plan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    """
    Setup Plan
    """
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def plansetup(self, ctx, address, name, verify: bool, uname=None, psw=None):
        if verify and (uname is None or psw is None):
            await ctx.send(f"{ctx.author.mention} please provide a valid username and password")

        else:
            if verify:
                configuration = {
                    "address": address,
                    "serverName": name,
                    "verify": verify,
                    "uname": uname,
                    "password": psw
                }
            else:
                configuration = {
                    "address": address,
                    "serverName": name,
                    "verify": verify
                }

            await ctx.send(f"{ctx.author.mention} the following information will be listed for your plan configuration:\n{configuration}")

            try:
                open(f"./modules/{name}/config.json", "x")
                await ctx.send(f"{ctx.author.mention} a server has taken that name already, please try a different name.")
            
            except:
                os.mkdir(f"./modules/{name}")
                with open(f"./modules/{name}/config.json", "w") as outfile:
                    json.dump(configuration, outfile, indent=4)

                conn = sqlite3.connect("./data/guildSettings.db")

                sql = f"""INSERT INTO PlanServers(ID,name) 
                        VALUES(?,?)"""
                    
                cur = conn.cursor()
                args = (ctx.guild.id, name,)
                cur.execute(sql, args)

                conn.commit()

                with open(f"./modules/config.json", "r") as json_file:
                    f = json.load(json_file)

                f['enabledModules'][name] = {
                    "configPath": f"./modules/{name}/config.json"
                }

                with open(f"./modules/config.json", "w") as out:
                    json.dump(f, out, indent=4)

    """
    Repeat code functions
    """
    async def getPlanServer(self, ctx):
        conn = sqlite3.connect("./data/guildSettings.db")

        curr = conn.cursor()
        sql = f'''SELECT * FROM PlanServers 
                    WHERE ID=?'''
                
        args = (ctx.guild.id,)
        curr.execute(sql, args)
        try:
            server = curr.fetchone()[1]

        except TypeError:
            await ctx.send(f"{ctx.author.mention} Plan has not been setup for this server, if you believe this is an error please contact the server's administrator.")
            return None
        
        return server

    async def dictOut(self, ctx, title, dict_):
        embed = discord.Embed(title=f"Plan {title} Lookup", description=f"The results of {ctx.author}'s lookup", color=options.getEmbedColour(ctx.guild.id))
        embed.set_thumbnail(url=options.planLogo)
        
        for info in dict_:
            embed.add_field(name=info, value=dict_[info], inline=False)

        await ctx.send(embed=embed)

    """
    Player related commands
    """
    @commands.command()
    async def lastseen(self, ctx, name):
        srv = await self.getPlanServer(ctx)

        if srv is None:
            return

        ls = player.lastSeen(srv, name)
        
        await ctx.send(f"{ctx.author.mention} player, {name}, was last seen {ls}.")

    @commands.command()
    async def banned(self, ctx, name):
        srv = await self.getPlanServer(ctx)

        if srv is None:
            return

        banned = player.banned(srv, name)

        if banned:
            await ctx.send(f"{ctx.author.mention} player, {name}, is banned")

        else:
            await ctx.send(f"{ctx.author.mention} player, {name}, is not banned")

    @commands.command()
    async def playtime(self, ctx, name):
        srv = await self.getPlanServer(ctx)

        if srv is None:
            return

        pt = player.playtime(srv, name)

        await self.dictOut(ctx, "Playtime", pt)

    @commands.command()
    async def activity(self, ctx, name, q=None):
        if q is not None:
            """
            Some printout about how the activity index is calculated
            """
            pass

        else:
            srv = await self.getPlanServer(ctx)

            if srv is None:
                return

            activity = player.activity(srv, name)

            embed = discord.Embed(title="Plan Activity Lookup", description=f"The results of {ctx.author}'s lookup", color=options.getEmbedColour(ctx.guild.id))
            embed.set_thumbnail(url=options.planLogo)

            embed.add_field(name=activity[0], value=activity[1])

            await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx, name):
        srv = await self.getPlanServer(ctx)

        if srv is None:
            return

        ping = player.ping(srv, name)

        await self.dictOut(ctx, "Ping", ping)

    @commands.command()
    async def firstjoin(self, ctx, name):
        srv = await self.getPlanServer(ctx)

        if srv is None:
            return

        first = player.firstJoin(srv, name)

        await ctx.send(f"{ctx.author.mention} player, {name}, first joined on {first}.")

def setup(bot):
    bot.add_cog(Plan(bot))
