import requests
import json

from modules import modulesConfig

def getData(serverName, name):
    with open(modulesConfig.getConfig()['enabledModules'][serverName]['configPath'], 'r') as json_file:
        config = json.load(json_file)

    data = None
    
    if config['verify']:
        data = requests.get(f"https://{config['address']}/auth/login?user={config['uname']}&password={config['password']}")
    
    data = requests.get(f"{config['address']}/v1/player?player={name}").json()

    return data

def lastSeen(serverName, name):
    data = getData(serverName, name)

    try:
        info = data['info']
    except:
        return None

    return info.get('last_seen', 'Never')

def playtime(serverName, name):
    data = getData(serverName, name)

    try:
        info = data['online_activity']
    except:
        return None
    
    total = info.get('playtime_30d', '0s')
    active = info.get('active_playtime_30d', '0s')
    afk = info.get('afk_time_30d')

    sessionCount = info.get('session_count_30d')

    return {
        'Total Playtime': total,
        'Total Active Time': active,
        'AFK Time': afk,
        'Sessions': sessionCount
    }

def activity(serverName, name):
    data = getData(serverName, name)

    try:
        info = data['info']
    except:
        return None

    group = info.get('activity_index_group', 'Inactive')
    score = info.get('activity_index')

    return [group, score]

def ping(serverName, name):
    data = getData(serverName, name)

    try:
        info = data['info']
    except:
        return None

    average = info.get('average_ping', '0 ms')
    best = info.get('best_ping', '0ms ')
    worst = info.get('worst_ping', '0 ms')

    return {
        'Average Ping': average,
        'Best Ping': best,
        'Worst Ping': worst
    }

def firstJoin(serverName, name):
    data = getData(serverName, name)

    try:
        info = data['info']
    except:
        return None

    return info.get('registered', 'Never')

def banned(serverName, name):
    data = getData(serverName, name)

    try:
        info = data['info']
    except:
        return None
    
    return info.get('banned', False)
