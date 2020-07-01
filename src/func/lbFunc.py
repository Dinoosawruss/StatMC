import json
import random

def add(name):
    

    with open('./data/leaderboard.json') as json_file:
        data = json.load(json_file)

    for user in data['users']:
        if user['name'] == name:
            user['score'] += 1
            with open('./data/leaderboard.json', 'w') as outfile:
                json.dump(data, outfile)
            return

    data['users'].append({
        'name': name,
        'score': 1
    })


    with open('./data/leaderboard.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)

def getTop():
    

    leaderboard = []

    with open('./data/leaderboard.json') as json_file:
        data = json.load(json_file)

    for user in data['users']:
        leaderboard.append([user['score'], user['name']])

    leaderboard = sorted(leaderboard, key=lambda x: x[0], reverse=True)

    return leaderboard

def purge(reason, by):
    

    with open('./data/leaderboard.json') as json_file:
        data = json.load(json_file)

    name = f"{random.randint(0,9999)}.txt"
    f = open(f'./archive/{name}', "w")
    
    f.write(f"{data}\n\nPurged by: {by}\nReason {reason}")

    f.close()

    with open('./data/leaderboard.json', 'w') as json_file:
        json.dump({"users": []}, json_file)

