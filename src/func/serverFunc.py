import requests
import json

def getServerStatus(ip):
    server = requests.get(f"https://eu.mc-api.net/v3/server/ping/{ip}").json()
    if server['status'] and server['online']:
        desc = ""

        try:
            for i in server['description']['extra']:
                print(i['text'])
                desc += i['text']
        except:
            try:
                desc = server['description']['text']
            except:
                try:
                    desc = server['description']
                except:
                    desc = "Error"


        stats = {
            'ip': ip,
            'favicon': server['favicon'],
            'desc': desc,
            'ping': server['took'],
            'onlinePlayers': server['players']['online'],
            'maxPlayers': server['players']['max'],
            'version': server['version']['name'],
            'protocol': server['version']['protocol']
        }

        return stats 

    else:
        return server['error']
    
