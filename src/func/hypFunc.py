import datetime
import math
import requests
import json

from func import mojang
from func.hiddenVars import HYPIXEL_API_KEY

########################################################
#################### Game Modes ########################
########################################################

def arcade(name):
    data = requests.get(f"https://api.hypixel.net/player?key={HYPIXEL_API_KEY}&name={name}").json()

    if data['success']:
        arcade = data['player']['stats']['Arcade']
        
        stats = {
            'coins': arcade.get('coins', 0),
            'blockingDeadKills': arcade.get('kills_dayone', 0),
            'blockingDeadWins': arcade.get('wins_dayone', 0),
            
        }

def bedwars(name, t=None):
    data = requests.get(f"https://api.hypixel.net/player?key={HYPIXEL_API_KEY}&name={name}").json()

    if data['success']:
        bw = data['player']['stats']['Bedwars']
        achievements = data['player']['achievements']

        if t is None:
            stats = {
                'coins': bw.get(f'coins', 0),
                'streak': bw.get(f'winstreak', 0),
                'level': achievements.get('bedwars_level', 0),
                'diamondsCollected': bw.get(f'diamond_resources_collected_bedwars', 0),
                'emeraldsCollected': bw.get(f'emerald_resources_collected_bedwars', 0),
                'goldCollected': bw.get(f'gold_resources_collected_bedwars', 0),
                'ironCollected': bw.get(f'iron_resources_collected_bedwars', 0),
                'wins': bw.get(f'wins_bedwars', 0),
                'losses': bw.get(f'losses_bedwars', 0),
                'wl': bw.get(f'wins_bedwars', 0)/bw.get(f'losses_bedwars', 0),
                'kills': bw.get(f'kills_bedwars', 0),
                'deaths': bw.get(f'deaths_bedwars', 0), 
                'kd': bw.get(f'kills_bedwars', 0)/bw.get(f'deaths_bedwars', 0),
                'fkills': bw.get(f'final_kills_bedwars', 0),
                'fdeaths': bw.get(f'final_deaths_bedwars', 0),
                'fkd': bw.get(f'final_kills_bedwars', 0)/bw.get(f'final_deaths_bedwars', 0),
                'bedsBroke': bw.get(f'beds_broken_bedwars', 0)
            }

            return stats

        elif t[0].lower() == "s" or (t[0].lower() == "1" and len(t) == 1):
            key = "eight_one"

        elif t[0].lower() == "d" or (t[0].lower() == "2" and len(t) == 1):
            key = "eight_two"

        elif t[0].lower() == "t" or (t[0].lower() == "3" and len(t) == 1):
            key = "four_three"

        elif t[0].lower() == "f" or (t[0].lower() == "4" and len(t) == 1):
            key = "four_four"

        else:
            return None
        
        stats = {
            'streak': bw.get(f'{key}_winstreak', 0),
            'diamondsCollected': bw.get(f'{key}_diamond_resources_collected_bedwars', 0),
            'emeraldsCollected': bw.get(f'{key}_emerald_resources_collected_bedwars', 0),
            'goldCollected': bw.get(f'{key}_gold_resources_collected_bedwars', 0),
            'ironCollected': bw.get(f'{key}_iron_resources_collected_bedwars', 0),
            'wins': bw.get(f'{key}_wins_bedwars', 0),
            'losses': bw.get(f'{key}_losses_bedwars', 0),
            'wl': bw.get(f'{key}_wins_bedwars', 0)/bw.get(f'{key}_losses_bedwars', 0),
            'kills': bw.get(f'{key}_kills_bedwars', 0),
            'deaths': bw.get(f'{key}_deaths_bedwars', 0), 
            'kd': bw.get(f'{key}_kills_bedwars', 0)/bw.get(f'{key}_deaths_bedwars', 0),
            'fkills': bw.get(f'{key}_final_kills_bedwars', 0),
            'fdeaths': bw.get(f'{key}_final_deaths_bedwars', 0),
            'fkd': bw.get(f'{key}_final_kills_bedwars', 0)/bw.get(f'{key}_final_deaths_bedwars', 0),
            'bedsBroke': bw.get(f'{key}_beds_broken_bedwars', 0)
        }

        return stats

def buildbattle(name):
    data = requests.get(f"https://api.hypixel.net/player?key={HYPIXEL_API_KEY}&name={name}").json()

    if data['success']:
        try:
            mojang.nameToUUID(name)
        except: 
            return
        
        try:
            bb = data['player']['stats']['BuildBattle']
        except:
            return "NP"

        stats = {
            'score': bb.get('score', 0),
            'gamesPlayed': bb.get('games_played', 0),
            'totalVotes': bb.get('total_votes', 0),
            'correctGuesses': bb.get('correct_guesses', 0),
            'soloWins': bb.get('wins_solo_normal', 0),
            'teamsWins': bb.get('wins_teams_normal', 0),
            'guessTheBuildWins': bb.get('wins_guess_the_build', 0),
            'proWins': bb.get('wins_solo_pro', 0)
        }

        return stats

def duels(name, t):
    data = requests.get(f"https://api.hypixel.net/player?key={HYPIXEL_API_KEY}&name={name}").json()

    duels = data['player']['stats']['Duels']

    if data['success']:
        if t is None:
            stats = {
                'coins': duels.get('coins', 0),
                'kills': duels.get('kills', 0),
                'deaths': duels.get('deaths', 0),
                'KD': round(duels.get('kills', 0)/duels.get('deaths', 0),2),
                'wins': duels.get('wins', 0),
                'losses': duels.get('losses', 0),
                'WL': round(duels.get('wins', 0)/duels.get('losses', 0),2),
                'arrowsShot': duels.get('bow_shots', 0),
                'arrowsHit': duels.get('bow_hits', 0),
                'HM': round(duels.get('bow_shots', 0)/duels.get('bow_hits', 0),2),
                'meleeSwings': duels.get('melee_swings', 0),
                'meleeHits': duels.get('melee_hits', 0),
                'MHM': round(duels.get('melee_hits', 0)/duels.get('melee_swings', 0),2)
            }
        
            return stats

        elif "tourn" in t.lower():
            key = "sw_tournament"
        
        elif "uhc" in t.lower():
            if "1" in t.lower():
                key = "uhc_duel"

            elif "2" in t.lower():
                key = "uhc_doubles"
            
            elif "4" in t.lower():
                key = "uhc_four"

            elif "m" in t.lower():
                key = "uhc_tournament"
        
        elif "op" in t.lower():
            if "1" in t.lower():
                key = "op_duels"
            
            if "2" in t.lower():
                key = "op_doubles"

        elif "skywar" in t.lower():
            if "1" in t.lower():
                key = "sw_duel"
            
            if "2" in t.lower():
                key = "sw_doubles"

        elif "blitz" in t.lower():
            key = "blitz_duel"

        elif "sumo" in t.lower():
            key = "sumo_duel"

        elif "classic" in t.lower():
            key = "classic_duel"

        elif "bridge" in t.lower():
            if "1" in t.lower():
                key = "bridge_duel"

            elif "2v2v2v2" in t.lower():
                key = "bridge_2v2v2v2"

            elif "2" in t.lower():
                key = "bridge_doubles"

            elif "3" in t.lower():
                key = "bridge_3v3v3v3"

            
            elif "4" in t.lower():
                key = "bridge_four"
            
        else:
            return None

        stats = {
                'kills': duels.get(f'{key}_kills', 0),
                'deaths': duels.get(f'{key}_deaths', 0),
                'KD': round(duels.get(f'{key}_kills', 0)/duels.get(f'{key}_deaths', 0),2),
                'wins': duels.get(f'{key}_wins', 0),
                'losses': duels.get(f'{key}_losses', 0),
                'WL': round(duels.get(f'{key}_wins', 0)/duels.get(f'{key}_losses', 0),2),
                'arrowsShot': duels.get(f'{key}_bow_shots', 0),
                'arrowsHit': duels.get(f'{key}_bow_hits', 0),
                'HM': round(duels.get(f'{key}_bow_hits', 0)/duels.get(f'{key}_bow_shots', 0),2),
                'meleeSwings': duels.get(f'{key}_melee_swings', 0),
                'meleeHits': duels.get(f'{key}_melee_hits', 0),
                'MHM': round(duels.get(f'{key}_melee_hits', 0)/duels.get(f'{key}_melee_swings', 0),2)
            }

        return stats

# def murder(name, t):
#     data = requests.get(f"https://api.hypixel.net/player?key={HYPIXEL_API_KEY}&name={name}").json()

#     if data['success']:
#         try:
#             uuid = mojang.nameToUUID(name)
#         except: 
#             return

#         if t is None:
#             stats = {
#                 'wins': data['']
#             }

def skyblock(name):
    data = requests.get(f"https://api.hypixel.net/player?key={HYPIXEL_API_KEY}&name={name}").json()

    if data['success']:
        try:
            uuid = mojang.nameToUUID(name)
        except: 
            return

        sbID = data['player']['stats']['SkyBlock']['profiles'][uuid]['profile_id']

        sbData = requests.get(f"https://api.hypixel.net/skyblock/profile?key={HYPIXEL_API_KEY}&profile={sbID}").json()
        print(f"https://api.hypixel.net/skyblock/profile?key={HYPIXEL_API_KEY}&profile={sbID}")

def skywars(name, t=None):
    data = requests.get(f"https://api.hypixel.net/player?key={HYPIXEL_API_KEY}&name={name}").json()

    if data['success']:
        sw = data['player']['stats']['SkyWars']

        if t is None:
            level = int(sw.get('levelFormatted', 0).replace("§f", "").replace("⋆", ""))

            if level >= 60:
                prestige = "mythic"
            elif level >= 50:
                prestige = "rainbow"
            elif level >= 45:
                prestige = "amethyst"
            elif level >= 40:
                prestige = "opal"
            elif level >= 35:
                prestige = "crystal"
            elif level >= 30:
                prestige = "ruby"
            elif level >= 25:
                prestige = "sapphire"
            elif level >= 20:
                prestige = "emerald"
            elif level >= 15:
                prestige = "aqua"
            elif level >= 10:
                prestige = "gold"
            elif level > 5:
                prestige = "Iron"
            else:
                prestige = "None"

            stats = {
                'level': level,
                'prestige': prestige,
                'coins': sw.get('coins', 0),
                'kills': sw.get('kills', 0),
                'assists': sw.get('assists', 0),
                'deaths': sw.get('deaths', 0),
                'KD': round(sw.get('kills', 0)/sw.get('deaths', 0),2),
                'wins': sw.get('wims', 0),
                'losses': sw.get('losses', 0),
                'WL': round(sw.get('wins', 0)/sw.get('losses', 0),2),
                'soul_well_uses': sw.get('soul_well', 0),
                'soul_well_leg': sw.get('soul_well_legendaries', 0),
                'purchased_souls': sw.get('paid_souls', 0),
                'gathered_souls': sw.get('souls_gathered', 0),
                'eggs_thrown': sw.get('egg_thrown', 0),
                'enderpearls_thrown': sw.get('enderpearls_thrown', 0),
                'blocks_broken': sw.get('blocks_broken', 0),
                'blocks_placed': sw.get('blocks_placed', 0),
                'arrows_shot': sw.get('arrows_shot', 0),
                'arrows_hit': sw.get('arrows_hit', 0),
                'arrows_missed': sw.get('arrows_shot', 0)-sw.get('arrows_hit', 0),
                'HM': round(sw.get('arrows_hit', 0)/(sw.get('arrows_shot', 0)-sw.get('arrows_hit', 0)),2)
            }

            return stats

        elif t.lower() == "solo": 
            key = "solo"
        
        elif t.lower() == "team" or t.lower() == "teams": 
            key = "team"
        
        elif t.lower() == "solo normal" or t.lower() == "normal solo": 
            key = "solo_normal"
        
        elif t.lower() == "solo insane" or t.lower() == "insane solo": 
            key = "solo_insane"

        elif t.lower() == "team normal" or t.lower() == "normal team" or t.lower() == "teams normal" or t.lower() == "normal teams": 
            key = "teams_normal"
        
        elif t.lower() == "teams insane" or t.lower() == "insane teams" or t.lower() == "team insane" or t.lower() == "insane teams": 
            key = "teams_insane"

        else:
            return None

        stats = {
            'kills': sw.get(f'kills_{key}', 0),
            'assists': sw.get(f'assists_{key}', 0),
            'deaths': sw.get(f'deaths_{key}', 0),
            'KD': round(sw.get(f'kills_{key}', 0)/sw.get(f'deaths_{key}', 0),2),
            'wins': sw.get(f'wins_{key}', 0),
            'losses': sw.get(f'losses_{key}', 0),
            'WL': round(sw.get(f'wins_{key}', 0)/sw.get(f'losses_{key}', 0),2)
        }
            
        return stats

########################################################
############### Gemeral Player Info ####################
########################################################

def player(name, uuid):
    data = requests.get(f"https://api.hypixel.net/player?key={HYPIXEL_API_KEY}&name={name}").json()
    friends = requests.get(f"https://api.hypixel.net/friends?key={HYPIXEL_API_KEY}&uuid={uuid}").json()

    if "rank" in data["player"] and data["player"]["rank"] != "NORMAL":
        rank = data["player"]["rank"]
    elif "monthlyPackageRank" in data["player"]:
        rank = data["player"]["monthlyPackageRank"]
    elif "newPackageRank" in data["player"]:
        rank = data["player"]["newPackageRank"]
    elif "packageRank" in data["player"]:
        rank = data["player"]["packageRank"]
    else:
        rank = "Non-Donor"

    if rank == "SUPERSTAR":
        rank = "MVP++"

    elif rank == "MVP_PLUS":
        rank = "MVP+"

    elif rank == "VIP_PLUS":
        rank = "VIP+"

    

    EXP = data['player']['networkExp']
    level = (math.sqrt(EXP + 15312.5) - (125/math.sqrt(2)) ) / (25 * math.sqrt(2))

    try:
        guildID = requests.get(f"https://api.hypixel.net/findGuild?key={HYPIXEL_API_KEY}&byUuid={uuid}").json()['guild']
        #print(guildID)
        guild = requests.get(f"https://api.hypixel.net/guild?key={HYPIXEL_API_KEY}&id={guildID}").json()['guild']
        #print(guild)
    except:
        guild = {'name': None, 'members': []}

    if data['success']:
        stats = {
            'rank': rank,
            'level': round(level,2),
            'karma': data['player']['karma'],
            'achievementPoints': data['player']['achievementPoints'],
            'firstLogin': datetime.datetime.fromtimestamp(data['player']['firstLogin'] // 1000.0),
            'lastLogin': datetime.datetime.fromtimestamp(data['player']['lastLogin'] // 1000.0),
            'friendsCount': len(friends['records']),
            'guildName': guild['name'],
            'guildMemberCount': len(guild['members']) 
        }
    

    return stats


def friends(uuid):
    data = requests.get(f"https://api.hypixel.net/friends?key={HYPIXEL_API_KEY}&uuid={uuid}").json()
   
    if data['success']:
        stats = []
        for friend in data['records']: 
            if friend['uuidReceiver'] == uuid:
                friendUUID = friend['uuidSender']

            else:
                friendUUID = friend['uuidReceiver']

            stats.append(
                {
                    'name': mojang.uuidToName(friendUUID),
                    'dateAdded': datetime.datetime.fromtimestamp(friend['started'] // 1000.0)
                }
            )

        return stats

def parkour(name):
    data = requests.get(f"https://api.hypixel.net/player?key={HYPIXEL_API_KEY}&name={name}").json()

    pk = data['player']['parkourCompletions']

    out = []

    for key in pk:
        quickest = pk[key][0]['timeTook']
        if len(pk[key]) > 1:
            for attempt in pk[key]:
                if attempt['timeTook'] < quickest:
                    quickest = attempt['timeTook']
        
        quickest = round(quickest/1000, 2)
        if quickest > 60:
            quickestMins = quickest//60
            quickestSecs = round(quickest-(quickestMins*60),2)

            quickest = f"{quickestMins} minutes and {quickestSecs} seconds"
        
        else:
            quickest = f"{quickest} seconds"
            
        out.append([key, quickest])

    return out

########################################################
#################### Guild Info ########################
########################################################

def guild(name, t=None):
    guildID = requests.get(f"https://api.hypixel.net/findGuild?key={HYPIXEL_API_KEY}&byName={name}").json()['guild']
    
    guild = requests.get(f"https://api.hypixel.net/guild?key={HYPIXEL_API_KEY}&id={guildID}").json()['guild']
    
    if t is None:
        EXP = guild['exp']
        print(EXP)
        if EXP <= 100000:
            level = 0
        elif EXP >= 100000 and EXP < 250000:
            level = 1
        elif EXP >= 250000 and EXP < 500000:
            level = 2
        elif EXP >= 500000 and EXP < 1000000:
            level = 3
        elif EXP >= 1000000 and EXP < 1750000:
            level = 4
        elif EXP >= 1750000 and EXP < 2750000:
            level = 5
        elif EXP >= 2750000 and EXP < 4000000:
            level = 6
        elif EXP >= 4000000 and EXP < 5500000:
            level = 7
        elif EXP >= 5500000 and EXP < 1500000:
            level = 8
        elif EXP >= 1500000 and EXP < 7500000:
            level = 9
        elif EXP >= 7500000 and EXP < 10000000:
            level = 10
        else:
            EXP -= 7500000
            level = 10 + (EXP//3000000)

        try:
            desc = guild['description']
            
        except:
            desc = "None"

        try:
            tag = guild['tag']
            
        except:
            tag = "None"

        try:
            public = guild['publiclyListed']

        except:
            public = False

        try:
            joinable = guild['joinable']
        
        except:
            joinable = False

        try:
            preferedGames = guild['preferredGames']
        
        except:
            preferedGames = "NONE"

        stats = {
            'name': guild['name'],
            'tag': tag,
            'created': datetime.datetime.fromtimestamp(guild['created'] // 1000.0),
            'memberCount': len(guild['members']),
            'level': level,
            'desc': desc,
            'public': public,
            'joinable': joinable,
            'preferedGames': preferedGames
        }

        return stats
    
    elif t.lower()[0] == "m":
        stats = []
        for member in guild['members']:
            stats.append(
                {
                    'name': mojang.uuidToName(member['uuid']),
                    'rank': member['rank'],
                    'dateJoined': datetime.datetime.fromtimestamp(member['joined'] // 1000.0)
                }
            )

        return stats