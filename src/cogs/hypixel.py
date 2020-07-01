import discord
from discord.ext import commands

from func import mojang, options, lbFunc, hypFunc

class Hypixel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def statEmbed(self, ctx, out):
        embed = discord.Embed()
        embed=discord.Embed(title="Hypixel Stats Lookup", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
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
            embed=discord.Embed(title="Hypixel Stats Lookup", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
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
                embed=discord.Embed(title="Hypixel Stats Lookup", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
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

                if t is None:
                    

                    out = {'name':name,'tag':'Bedwars Stats (Overall)','checkName':'Iron Collected','stats':[{'name': 'Coins','key': stats['coins']},{'name': 'Winstreak','key': stats['streak']},{'name': 'Bedwars Level','key': stats['level']},{'name': 'Emeralds Collected','key': stats['emeraldsCollected']},{'name': 'Diamonds Collected','key': stats['diamondsCollected']},{'name': 'Gold Collected','key': stats['goldCollected']},{'name': 'Iron Collected','key': stats['ironCollected']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': round(stats['wl'],2)},{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': round(stats['kd'],2)},{'name': 'Final Kills','key': stats['fkills']},{'name': 'Final Deaths','key': stats['fdeaths']},{'name': 'Final K/D Ratio','key': round(stats['fkd'],2)},{'name': 'Beds Broken','key': stats['bedsBroke']}]}
                    
                    await self.statEmbed(ctx, out)

                elif t[0].lower() == "s" or (t[0].lower() == "1" and len(t) == 1):
                    

                    out = {'name':name,'tag':'Bedwars Stats (Solo)','checkName':'Iron Collected','stats':[{'name': 'Winstreak','key': stats['streak']},{'name': 'Emeralds Collected','key': stats['emeraldsCollected']},{'name': 'Diamonds Collected','key': stats['diamondsCollected']},{'name': 'Gold Collected','key': stats['goldCollected']},{'name': 'Iron Collected','key': stats['ironCollected']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': round(stats['wl'],2)},{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': round(stats['kd'],2)},{'name': 'Final Kills','key': stats['fkills']},{'name': 'Final Deaths','key': stats['fdeaths']},{'name': 'Final K/D Ratio','key': round(stats['fkd'],2)},{'name': 'Beds Broken','key': stats['bedsBroke']}]}         
                    
                    await self.statEmbed(ctx, out)

            
                elif t[0].lower() == "d" or (t[0].lower() == "2" and len(t) == 1):
                    

                    out = {'name':name,'tag':'Bedwars Stats (Doubles)','checkName':'Iron Collected','stats':[{'name': 'Winstreak','key': stats['streak']},{'name': 'Emeralds Collected','key': stats['emeraldsCollected']},{'name': 'Diamonds Collected','key': stats['diamondsCollected']},{'name': 'Gold Collected','key': stats['goldCollected']},{'name': 'Iron Collected','key': stats['ironCollected']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': round(stats['wl'],2)},{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': round(stats['kd'],2)},{'name': 'Final Kills','key': stats['fkills']},{'name': 'Final Deaths','key': stats['fdeaths']},{'name': 'Final K/D Ratio','key': round(stats['fkd'],2)},{'name': 'Beds Broken','key': stats['bedsBroke']}]}
                    
                    await self.statEmbed (ctx, out)
                
                elif t[0].lower() == "t" or (t[0].lower() == "3" and len(t) == 1):
                    

                    out = {'name':name,'tag':'Bedwars Stats (3v3v3v3)','checkName':'Iron Collected','stats':[{'name': 'Winstreak','key': stats['streak']},{'name': 'Emeralds Collected','key': stats['emeraldsCollected']},{'name': 'Diamonds Collected','key': stats['diamondsCollected']},{'name': 'Gold Collected','key': stats['goldCollected']},{'name': 'Iron Collected','key': stats['ironCollected']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': round(stats['wl'],2)},{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': round(stats['kd'],2)},{'name': 'Final Kills','key': stats['fkills']},{'name': 'Final Deaths','key': stats['fdeaths']},{'name': 'Final K/D Ratio','key': round(stats['fkd'],2)},{'name': 'Beds Broken','key': stats['bedsBroke']}]
                    }
                    
                    await self.statEmbed(ctx,out)
            
                elif t[0].lower() == "f" or (t[0].lower() == "4" and len(t) == 1):
                    

                    out = {'name':name,'tag':'Bedwars Stats (4v4v4v4)','checkName':'Iron Collected','stats':[{'name': 'Winstreak','key': stats['streak']},{'name': 'Emeralds Collected','key': stats['emeraldsCollected']},{'name': 'Diamonds Collected','key': stats['diamondsCollected']},{'name': 'Gold Collected','key': stats['goldCollected']},{'name': 'Iron Collected','key': stats['ironCollected']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': round(stats['wl'],2)},{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': round(stats['kd'],2)},{'name': 'Final Kills','key': stats['fkills']},{'name': 'Final Deaths','key': stats['fdeaths']},{'name': 'Final K/D Ratio','key': round(stats['fkd'],2)},{'name': 'Beds Broken','key': stats['bedsBroke']}]}

                    await self.statEmbed(ctx,out)
                
                else:
                    await ctx.send(f"{ctx.author.mention} the sub-mode provided was not recognised...")



            elif mode.lower() == "buildbattle":
                stats = hypFunc.buildbattle(name)
                if stats == "NP":
                    await ctx.send(f"{ctx.author.mention} this user has never played Build Battle")
                    return
                
                out = {'name':name,'tag':'Build Battle Stats','checkName':'Correct Guesses (GTB)','stats':[{'name': 'Score','key': stats['score']},{'name': 'Games Played','key': stats['gamesPlayed']},{'name': 'Total Votes','key': stats['totalVotes']},{'name': 'Correct Guesses (GTB)','key': stats['correctGuesses']},{'name': 'Solo Wins','key': stats['soloWins']},{'name': 'Teams Wins','key': stats['teamsWins']},{'name': 'Guess The Build Wins','key': stats['guessTheBuildWins']},{'name': 'Pro Wins','key': stats['proWins']}]
                }

                await self.statEmbed(ctx,out)

            elif mode.lower() == "duels":
                
                stats = hypFunc.duels(name, t)
                # except:
                #     await ctx.send(f"{ctx.author.mention} this user has never played Duels")
                #     return

                if t is None:
                    out = {'name':name,'tag':'Duels Stats (Overall)','checkName':'Coins','stats':[{'name': 'Coins','key': stats['coins']},{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                    await self.statEmbed(ctx,out)

                elif "tourn" in t.lower():
                    out = {'name':name,'tag':'Duels Stats (SW Tournament)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                    await self.statEmbed(ctx,out)

                elif "uhc" in t.lower():
                    if "1" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (UHC 1v1)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                        await self.statEmbed(ctx,out)

                    elif "2" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (UHC 2v2)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                        await self.statEmbed(ctx,out)

                    
                    elif "4" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (UHC 4v4)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                        await self.statEmbed(ctx,out)

                    elif "m" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (UHC Meetup)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                        await self.statEmbed(ctx,out)
                
                elif "op" in t.lower():
                    if "1" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (OP 1v1)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                        await self.statEmbed(ctx,out)
                    
                    if "2" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (OP 2v2)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                        await self.statEmbed(ctx,out)

                elif "skywar" in t.lower():
                    if "1" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (SkyWars 1v1)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                        await self.statEmbed(ctx,out)
                    
                    if "2" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (SkyWars 2v2)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                        await self.statEmbed(ctx,out)

                elif "blitz" in t.lower():
                    out = {'name':name,'tag':'Duels Stats (Blitz 1v1)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                    await self.statEmbed(ctx,out)

                elif "sumo" in t.lower():
                    out = {'name':name,'tag':'Duels Stats (Sumo 1v1)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                    await self.statEmbed(ctx,out)

                elif "classic" in t.lower():
                    out = {'name':name,'tag':'Duels Stats (Classic 1v1)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                    await self.statEmbed(ctx,out)

                elif "bridge" in t.lower():
                    if "1" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (Bridge 1v1)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                        await self.statEmbed(ctx,out)

                    elif "2v2v2v2" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (Bridge 2v2v2v2)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                        await self.statEmbed(ctx,out)

                    elif "2" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (Bridge 2v2)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                        await self.statEmbed(ctx,out)

                    elif "3" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (Bridge 3v3v3v3)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                        await self.statEmbed(ctx,out)

                    
                    elif "4" in t.lower():
                        out = {'name':name,'tag':'Duels Stats (Bridge Teams)','checkName':'','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Arrows Shot','key': stats['arrowsShot']},{'name': 'Arrows Hit','key': stats['arrowsHit']},{'name': 'Arrow M/M Ratio','key': stats['HM']},{'name': 'Melee Swins','key': stats['meleeSwings']},{'name': 'Melee Hits','key': stats['meleeHits']},{'name': 'Melee H/M Ratio','key': stats['MHM']}]}

                        await self.statEmbed(ctx,out)


            elif mode.lower() == "skywars":

                try:
                    stats = hypFunc.skywars(name, t)
                except:
                    await ctx.send(f"{ctx.author.mention} this user has never played SkyWars")
                    return

                if t is None:
                    

                    out = {'name':name,'tag':'Skywars Stats (Overall)','checkName':'K/D Ratio','stats':[{'name': 'SkyWars Level','key': stats['level']},{'name': 'Prestige','key': stats['prestige']},{'name': 'Coins','key': stats['coins']},{'name': 'Kills','key': stats['kills']},{'name': 'Assists','key': stats['assists']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']},{'name': 'Soul Well Uses','key': stats['soul_well_uses']},{'name': 'Soul Well Legendaries','key': stats['soul_well_leg']},{'name': 'Purchased Souls','key': stats['purchased_souls']},{'name': 'Reaped Souls','key': stats['gathered_souls']},{'name': 'Blocks Broken','key': stats['blocks_broken']},{'name': 'Blocks Placed','key': stats['blocks_placed']},{'name': 'Arrows Shot','key': stats['arrows_shot']},{'name': 'Arrows Hit','key':stats['arrows_hit']},{'name':'Arrows Missed','key':stats['arrows_missed']},{'name':'Hit/Miss Ratio','key':stats['HM']}]}
                    
                    await self.statEmbed(ctx,out)

                elif t.lower() == "solo":
                    

                    out = {'name':name,'tag':'Skywars Stats (Solo)','checkName':'K/D Ratio','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Assists','key': stats['assists']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']}]}
                    
                    await self.statEmbed(ctx, out)

                elif t.lower() == "team" or t.lower() == "teams":
                    

                    out = {'name':name,'tag':'Skywars Stats (Teams)','checkName':'K/D Ratio','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Assists','key': stats['assists']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']}]}
                    
                    await self.statEmbed(ctx,out)

                elif t.lower() == "solo normal" or t.lower() == "normal solo":
                    

                    out = {'name':name,'tag':'Skywars Stats (Solo - Normal)','checkName':'K/D Ratio','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']}]}
                
                    await self.statEmbed(ctx,out)
                
                elif t.lower() == "solo insane" or t.lower() == "normal insane":
                    

                    out = {'name':name,'tag':'Skywars Stats (Solo - Insane)','checkName':'K/D Ratio','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']}]}
                
                    await self.statEmbed(ctx,out)

                elif t.lower() == "team normal" or t.lower() == "normal team" or t.lower() == "teams normal" or t.lower() == "normal teams":
                    

                    out = {'name':name,'tag':'Skywars Stats (Teams - Normal)','checkName':'K/D Ratio','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']}]}
                    
                    await self.statEmbed(ctx,out)
            
                elif t.lower() == "teams insane" or t.lower() == "insane teams" or t.lower() == "team insane" or t.lower() == "insane teams":
                    

                    out = {'name':name,'tag':'Skywars Stats (Teams - Insane)','checkName':'K/D Ratio','stats':[{'name': 'Kills','key': stats['kills']},{'name': 'Deaths','key': stats['deaths']},{'name': 'K/D Ratio','key': stats['KD']},{'name': 'Wins','key': stats['wins']},{'name': 'Losses','key': stats['losses']},{'name': 'W/L Ratio','key': stats['WL']}]}
                    
                    await self.statEmbed(ctx, out)

                else:
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
                    embed=discord.Embed(title="Hypixel Guild Lookup", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
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
                embed=discord.Embed(title="Hypixel Guild Lookup", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
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
            embed=discord.Embed(title="Hypixel Parkour Lookup", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
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
            embed=discord.Embed(title="Hypixel Guild Lookup", description=f"The results {ctx.author}'s lookup", color=options.embedColour)
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
