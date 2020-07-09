
import json

def getConfig():
    with open('./modules/config.json', 'r') as json_file:
        config = json.load(json_file)

    return config