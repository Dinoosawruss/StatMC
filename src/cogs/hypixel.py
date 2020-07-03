import discord
from discord.ext import commands

from func import mojang, options, lbFunc, hypFunc

class Hypixel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def statEmbed(self, ctx, out):
        embed = discord.Embed()
        embed=discord.Embed(title="Hypixel Stats Lookup", description=f"The results {ctx.author}'s lookup", color=options.getEmbedColour(ctx.guild.id))
        embed.set_thumbnail(url=options.hypixelLogo)
        embed.add_field(name="Current Username", value=f"{out['name']}", inline=False)
        embed.add_field(name=out['tag'], value="...", inline=False)

        for stat in out['stats']:
            embed.add_field(name=stat['name'], value=stat['key'], inline=stat['name'] != out['checkName'])

        await ctx.send(embed=embed)


    @commands.command()
    async def hypixel(self, ctx, get=None, name=None, mode=None, *, t=None):
        if get is None:
            embed = discord.Embed()
            embed=discord.Embed(title="Hypixel Stats Lookup", description=f"The results {ctx.author}'s lookup", color=options.getEmbedColour(ctx.guild.id))
            embed.set_thumbnail(url=options.hypixelLogo)
            embed.add_field(name="Current Supported Lookups", value=f"General (Rank, Level, Guild, etc)\nFriends\nGuild Info (General and Members)\nParkour Times\nBedwars (Solo, Doubles, 3v3v3v3 and 4v4v4v4)\nBuildBattle (General Overview)\nDuels (General, Sub-Modes)\nSkywars (General, Solo, Teams, Solo Normal, Solo Insane, Teams Normal, Teams Insane)", inline=False)
            embed.add_field(name="How the command works", value="?hypixel {type} {name} [mode] [sub-mode]\n\n**Lookup Types:**\n\n**Stats:**\n?hypixel stats {name} [mode] [type]\nExample - ?hypixel gamerboy80 bedwars solo\n\n**Guild:**\n?hypixel guild {name} [type] [page]\nExample - ?hypixel guild TescoFanClub members 2\n\n*If you do not provide the optional arguments (marked by square brackets - []) you will recieve a general overview.*", inline=False)
            await ctx.send(embed=embed)

        elif get.lower()[0] == "s":
            try:
                uuid = mojang.nameToUUID(name)
            except:
                await ctx.send(f"{ctx.author.mention} this username does not exist or could not be found...")
                return

            if mode is None:
                uuid = mojang.nameToUUID(name)
                stats = hypFunc.player(name, uuid)

                embed = discord.Embed()
                embed=discord.Embed(title="Hypixel Stats Lookup", description=f"The results {ctx.author}'s lookup", color=options.getEmbedColour(ctx.guild.id))
                embed.set_thumbnail(url=options.hypixelLogo)
                embed.add_field(name="Current Username", value=f"{name}", inline=False)
                embed.add_field(name="General Player Info", value="...", inline=False)
                embed.add_field(name="Rank", value=f"{stats['rank']}", inline=True)
                embed.add_field(name="Level", value=f"{stats['level']}", inline=True)
                embed.add_field(name="Achievement Points", value=f"{stats['achievementPoints']}", inline=True)
                embed.add_field(name="First Login", value=f"{stats['firstLogin']}", inline=True)
                embed.add_field(name="Last Login", value=f"{stats['lastLogin']}", inline=True)
                embed.add_field(name="Friends", value=f"{stats['friendsCount']}", inline=True)
                
                if stats['guildName'] is not None:
                    embed.add_field(name="Guild Name", value=f"{stats['guildName']}", inline=True)
                    embed.add_field(name="Guild Members", value=f"{stats['guildMemberCount']}", inline=True)
                await ctx.send(embed=embed)

            elif mode.lower() == "bedwars":
                try:
                    stats = hypFunc.bedwars(name, t)
                except:
                    await ctx.send(f"{ctx.author.mention} this user has never played Bedwars")
                    return
                
                defaultStats = [{'name': 'Winstreak','key': stats['streak']},{'name': 'Emeralds Collected','key': stats['emeraldsCollected']},{'name': 'Diamonds Collected','key': stats['diamondsCollected']},{'name': 'Gold Collected','key': stats['goldCollected']},{'name': 'Iron Collected','key': stats['ironCollected']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': round(stats['wl'],2)},{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': round(stats['kd'],2)},{'name': 'Final Kills','key': stats['fkills']},{'name': 'Final Deaths','key': stats['fdeaths']},{'name': 'Final K/D Ratio','key': round(stats['fkd'],2)},{'name': 'Beds Broken','key': stats['bedsBroke']}]

                submodes = [
                    {
                        "stats": defaultStats + [{'name': 'Coins','key': stats.get('coins')},{'name': 'Winstreak','key': stats['streak']},{'name': 'Bedwars Level','key': stats.get('level')}]
                    },
                    {
                        "identifierStr": "s",
                        "identifierInt": "1",
                        "customTag": "Solo"
                    },
                    {
                        "identifierStr": "d",
                        "identifierInt": "2",
                        "customTag": "Doubles"
                    },
                    {
                        "identifierStr": "t",
                        "identifierInt": "3",
                        "customTag": "3v3v3v3"
                    },
                    {
                        "identifierStr": "f",
                        "identifierInt": "4",
                        "customTag": "4v4v4v4"
                    }
                ]

                for mode in submodes:
                    if t == mode.get("identifierStr", None) or t == mode.get("identifierInt", None):
                        stats = {'name':name,'tag':f'Bedwars Stats ({mode.get("customTag", "Overall")})','checkName':'Iron Collected','stats':mode.get("stats", defaultStats)}
                        await self.statEmbed(ctx,mode.get("stats", stats))
                        return

                
                await ctx.send(f"{ctx.author.mention} the sub-mode provided was not recognised...")

            elif mode.lower() == "buildbattle":
                stats = hypFunc.buildbattle(name)
                if stats == "NP":
                    await ctx.send(f"{ctx.author.mention} this user has never played Build Battle")
                    return
                
                out = {'name':name,'tag':'Build Battle Stats','checkName':'Correct Guesses (GTB)','stats':[{'name': 'Score','key': stats['score']},{'name': 'Games Played','key': stats['gamesPlayed']},{'name': 'Total Votes','key': stats['totalVotes']},{'name': 'Correct Guesses (GTB)','key': stats['correctGuesses']},{'name': 'Solo Wins','key': stats['soloWins']},{'name': 'Teams Wins','key': stats['teamsWins']},{'name': 'Guess The Build Wins','key': stats['guessTheBuildWins']},{'name': 'Pro Wins','key': stats['proWins']}]}

                await self.statEmbed(ctx,out)

            elif mode.lower() == "duels":
                
                stats = hypFunc.duels(name, t)
                # except:
                #     await ctx.send(f"{ctx.author.mention} this user has never played Duels")
                #     return

                defaultStats = [{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]

                if t is None:
                    extras = [{'name': 'Coins','key': stats['coins']}]
                    out = {'name':name,'tag':'Duels Stats (Overall)','checkName':'Coins','stats':extras + defaultStats}

                elif "tourn" in t.lower():
                    out = {'name':name,'tag':'Duels Stats (SW Tournament)','checkName':'','stats':defaultStats}

                elif "uhc" in t.lower():
                    if "1" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (UHC 1v1)','checkName':'','stats':defaultStats}

                    elif "2" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (UHC 2v2)','checkName':'','stats':defaultStats}

                    elif "4" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (UHC 4v4)','checkName':'','stats':defaultStats}                        

                    elif "m" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (UHC Meetup)','checkName':'','stats':defaultStats}    
                
                elif "op" in t.lower():
                    if "1" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (OP 1v1)','checkName':'','stats':defaultStats}

                    if "2" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (OP 2v2)','checkName':'','stats':defaultStats}                       

                elif "skywar" in t.lower():
                    if "1" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (SkyWars 1v1)','checkName':'','stats':defaultStats} 
                    
                    if "2" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (SkyWars 2v2)','checkName':'','stats':defaultStats}

                elif "blitz" in t.lower():
                    out = {'name':name,'tag':'Duels Stats (Blitz 1v1)','checkName':'','stats':defaultStats}

                elif "sumo" in t.lower():
                    out = {'name':name,'tag':'Duels Stats (Sumo 1v1)','checkName':'','stats':defaultStats}                    

                elif "classic" in t.lower():
                    out = {'name':name,'tag':'Duels Stats (Classic 1v1)','checkName':'','stats':defaultStats}

                elif "bridge" in t.lower():
                    if "1" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (Bridge 1v1)','checkName':'','stats':defaultStats}

                    elif "2v2v2v2" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (Bridge 2v2v2v2)','checkName':'','stats':defaultStats} 

                    elif "2" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (Bridge 2v2)','checkName':'','stats':defaultStats}

                    elif "3" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (Bridge 3v3v3v3)','checkName':'','stats':defaultStats}

                    elif "4" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (Bridge Teams)','checkName':'','stats':defaultStats}             

                await self.statEmbed(ctx,out)

            elif mode.lower() == "skywars":

                try:
                    stats = hypFunc.skywars(name, t)
                except:
                    await ctx.send(f"{ctx.author.mention} this user has never played SkyWars")
                    return

                defaultStats = [{'name': 'Kills','key': stats['kills']},{'name': 'Assists','key': stats['assists']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']}]
                defaultStats_ = [{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']}]
                
                submodes = [
                    {
                        "stats": {'name':name,'tag':'Skywars Stats (Overall)','checkName':'K/D Ratio','stats':[{'name': 'SkyWars Level','key': stats['level']},{'name': 'Prestige','key': stats['prestige']},{'name': 'Coins','key': stats['coins']},defaultStats,{'name': 'Soul Well Uses','key': stats['soul_well_uses']},{'name': 'Soul Well Legendaries','key': stats['soul_well_leg']},{'name': 'Purchased Souls','key': stats['purchased_souls']},{'name': 'Reaped Souls','key': stats['gathered_souls']},{'name': 'Blocks Broken','key': stats['blocks_broken']},{'name': 'Blocks Placed','key': stats['blocks_placed']},{'name': 'Arrows Shot','key': stats['arrows_shot']},{'name': 'Arrows Hit','key':stats['arrows_hit']},{'name':'Arrows Missed','key':stats['arrows_missed']},{'name':'Hit/Miss Ratio','key':stats['HM']}]}
                    },
                    {
                        "identifierStr": "solo",
                        "customTag": "Solo"
                    },
                    {
                        "identifierStr": "Team",
                        "customTag": "Teams"
                    },
                    {
                        "identifierStr": "solo normal",
                        "customTag": "Solo - Normal",
                        "stats": defaultStats_
                    },
                    {
                        "identifierStr": "solo insane",
                        "customTag": "Solo - Insane",
                        "stats": defaultStats_
                    },
                    {
                        "identifierStr": "teams normal",
                        "customTag": "Teams - Normal",
                        "stats": defaultStats_
                    },
                    {
                        "identifierStr": "teams insane",
                        "customTag": "Teams - Insane",
                        "stats": defaultStats_
                    }
                ]

                for mode in submodes:
                    if t.lower() == mode.get("identifierStr", None):
                        stats = {'name':name,'tag':f'Skywars Stats ({mode.get("customTag", "Overall")})','checkName':'','stats':mode.get("stats", defaultStats)}
                        await self.statEmbed(ctx,mode.get("stats", stats))
                        return

                
                await ctx.send(f"{ctx.author.mention} the sub-mode provided was not recognised...")

            elif mode.lower() == "skyblock":
                await ctx.send(f"{ctx.author.mention} for hypixel skyblock please use `?skyblock`")
                
            else:
                await ctx.send(f"{ctx.author.mention} the game provided was not recognised...")

            lbFunc.add(name)


        elif get.lower()[0] == "g":
            if mode is None:
                stats = hypFunc.guild(name)

                if stats['name'] is not None:
                    embed = discord.Embed()
                    embed=discord.Embed(title="Hypixel Guild Lookup", description=f"The results {ctx.author}'s lookup", color=options.getEmbedColour(ctx.guild.id))
                    embed.set_thumbnail(url=options.hypixelLogo)
                    embed.add_field(name="Guild Name", value=stats['name'], inline=False)
                    embed.add_field(name="Guild Information", value="...", inline=False)

                    embed.add_field(name="Name", value=stats['name'], inline=False)
                    embed.add_field(name="Tag", value=stats['tag'], inline=False)
                    embed.add_field(name="Creation Date", value=stats['created'], inline=False)

                    embed.add_field(name="Member Count", value=stats['memberCount'], inline=False)
                    embed.add_field(name="Level", value=stats['level'], inline=False)
                    embed.add_field(name="Description", value=stats['desc'], inline=False)
                    embed.add_field(name="Joinable", value=stats['joinable'], inline=False)

                    if stats['preferedGames'] != "NONE":
                        pg = f""
                        for i in stats['preferedGames']:
                            pg += f"{i}\n"
                        
                    else:
                        pg = "NONE"

                    embed.add_field(name="Prefered Games", value=pg, inline=False)
                
                    await ctx.send(embed=embed)

                else:
                    await ctx.send(f"{ctx.author.mention} that user is not in a guild...")

            
            elif mode.lower()[0] == "m":
                await ctx.send(f"WARNING: {ctx.author.mention} guild member look-ups can be slow. Please wait and do not spam the command")
                
                members = hypFunc.guild(name, "m")
                guild = hypFunc.guild(name)

                embed = discord.Embed()
                embed=discord.Embed(title="Hypixel Guild Lookup", description=f"The results {ctx.author}'s lookup", color=options.getEmbedColour(ctx.guild.id))
                embed.set_thumbnail(url=options.hypixelLogo)
                embed.add_field(name="Guild Name", value=guild['name'], inline=False)
                embed.add_field(name=f"Guild Members - {guild['memberCount']}", value="...", inline=False)

                if len(members) <= 10:
                    for member in members:
                        embed.add_field(name=member['name'], value=f"{member['rank']}\nJoined: {member['dateJoined']}", inline=False)

                else:
                    page = t

                    if page is None:
                        for i in range(10):
                            member = members[i]
                            embed.add_field(name=member['name'], value=f"{member['rank']}\nJoined: {member['dateJoined']}", inline=False)

                        embed.add_field(name="...", value=f"Page 1/{len(members)//10}", inline=False)

                    else:
                        page = int(t)
                        for i in range(10*page-1,10*page):
                            try:
                                member = members[i]
                            except:
                                break

                            embed.add_field(name=member['name'], value=f"{member['rank']}\nJoined: {member['dateJoined']}", inline=False)
                        
                        embed.add_field(name="...", value=f"Page {page}/{len(members)//10}", inline=False)

                await ctx.send(embed=embed)
        
        elif get.lower()[0] == "p":
            try:
                uuid = mojang.nameToUUID(name)
            except:
                await ctx.send(f"{ctx.author.mention} this username does not exist or could not be found...")
                return

            times = hypFunc.parkour(name)

            embed = discord.Embed()
            embed=discord.Embed(title="Hypixel Parkour Lookup", description=f"The results {ctx.author}'s lookup", color=options.getEmbedColour(ctx.guild.id))
            embed.set_thumbnail(url=options.hypixelLogo)
            embed.add_field(name="Name", value=name, inline=False)
            embed.add_field(name="Times", value="...", inline=False)

            for time in times:
                embed.add_field(name=time[0], value=f"{time[1]}", inline=False)

            await ctx.send(embed=embed)
        
        elif get.lower()[0] == "f":
            try:
                uuid = mojang.nameToUUID(name)
            except:
                await ctx.send(f"{ctx.author.mention} this username does not exist or could not be found...")
                return

            await ctx.send(f"WARNING: {ctx.author.mention} friend look-ups can be slow. Please wait and do not spam the command")
                
            friends = hypFunc.friends(uuid)
            

            embed = discord.Embed()
            embed=discord.Embed(title="Hypixel Guild Lookup", description=f"The results {ctx.author}'s lookup", color=options.getEmbedColour(ctx.guild.id))
            embed.set_thumbnail(url=options.hypixelLogo)
            embed.add_field(name="Name", value=mojang.uuidToName(uuid), inline=False)
            embed.add_field(name=f"Friends - {len(friends)}", value="...", inline=False)

            if len(friends) <= 10:
                for friend in friends:
                    embed.add_field(name=f"`{friends['name']}`", value=f"Added: {friends['dateAdded']}", inline=False)

            else:
                page = t

                if page is None:
                    for i in range(10):
                        friend = friends[i]
                        embed.add_field(name=f"`{friend['name']}`", value=f"Added: {friend['dateAdded']}", inline=False)

                    embed.add_field(name="...", value=f"Page 1/{len(friends)//10}", inline=False)

                else:
                    page = int(t)
                    for i in range(10*page-1,10*page):
                        try:
                            friend = friends[i]
                        except:
                            break

                        embed.add_field(name=f"`{friend['name']}`", value=f"Added: {friend['dateAdded']}", inline=False)
                    
                    embed.add_field(name="...", value=f"Page {page}/{len(friends)//10}", inline=False)

            await ctx.send(embed=embed)

            
def setup(bot):
    bot.add_cog(Hypixel(bot))
