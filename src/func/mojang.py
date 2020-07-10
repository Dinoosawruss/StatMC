import requests
import json
from base64 import b64decode

from bs4 import BeautifulSoup    
import requests

def nameToUUID(name):
    
    

    url = "https://api.mojang.com/profiles/minecraft"

    x = requests.post(url, json = [name])

    return json.loads(x.text)[0]['id']

def nameToDashUUID(name):
    
    

    url = "https://api.mojang.com/profiles/minecraft"


    x = requests.post(url, json = [name])

    uuid = json.loads(x.text)[0]['id']

    arr = []
    for i in uuid:
        arr.append(i)

    arr.insert(8, "-")
    arr.insert(13, "-")
    arr.insert(18, "-")
    arr.insert(23, "-")

    uuid = ""

    for i in arr:
        uuid += i

    return uuid

def uuidToName(uuid):
    return uuidToNameHistory(uuid)[len(uuidToNameHistory(uuid))-1]

def uuidToNameHistory(uuid):
    
    

    out = []

    url = f"https://api.mojang.com/user/profiles/{uuid}/names"

    x = requests.get(url)
    x = json.loads(x.text)
    
    for username in x:
        out.append(username['name'])

    return out

capes = [ { 'url': '953cac8b779fe41383e675ee2b86071a71658f2180f56fbce8aa315ea70e2ed6', 'name': '2011 Minecon', 'image': '2011_minecon.png' }, { 'url': 'a2e8d97ec79100e90a75d369d1b3ba81273c4f82bc1b737e934eed4a854be1b6', 'name': '2012 Minecon', 'image': '2012_minecon.png' }, { 'url': '153b1a0dfcbae953cdeb6f2c2bf6bf79943239b1372780da44bcbb29273131da', 'name': '2013 Minecon', 'image': '2013_minecon.png' }, { 'url': 'b0cc08840700447322d953a02b965f1d65a13a603bf64b17c803c21446fe1635', 'name': '2015 Minecon', 'image': '2015_minecon.png' }, { 'url': 'e7dfea16dc83c97df01a12fabbd1216359c0cd0ea42f9999b6e97c584963e980', 'name': '2016 Minecon', 'image': '2016_minecon.png' }, { 'url': '17912790ff164b93196f08ba71d0e62129304776d0f347334f8a6eae509f8a56', 'name': 'Realms Map Maker', 'image': 'realms.png' }, { 'url': '5786fe99be377dfb6858859f926c4dbc995751e91cee373468c5fbf4865e7151', 'name': 'New Mojang', 'image': 'new_mojang.png' }, { 'url': '1bf91499701404e21bd46b0191d63239a4ef76ebde88d27e4d430ac211df681e', 'name': 'Translator', 'image': 'translator.png' }, { 'url': 'ae677f7d98ac70a533713518416df4452fe5700365c09cf45d0d156ea9396551', 'name': 'Mojira Moderator', 'image': 'mojira.png' }, { 'url': 'ca35c56efe71ed290385f4ab5346a1826b546a54d519e6a3ff01efa01acce81', 'name': 'Cobalt', 'image': 'cobalt.png' }, { 'url': '8f120319222a9f4a104e2f5cb97b2cda93199a2ee9e1585cb8d09d6f687cb761', 'name': 'Old Mojang', 'image': 'old_mojang.png' }, { 'url': '3efadf6510961830f9fcc077f19b4daf286d502b5f5aafbd807c7bbffcaca245', 'name': 'Scrolls', 'image': 'scrolls.png' }, { 'url': '2262fb1d24912209490586ecae98aca8500df3eff91f2a07da37ee524e7e3cb6', 'name': 'Chinese Translator', 'image': 'translator.png' }, { 'url': 'ca29f5dd9e94fb1748203b92e36b66fda80750c87ebc18d6eafdb0e28cc1d05f', 'name': 'Japanese Translator (Exclusive)', 'image': 'translator.png' }, { 'url': 'bcfbe84c6542a4a5c213c1cacf8979b5e913dcb4ad783a8b80e3c4a7d5c8bdac', 'name': 'dannyBstyle (Exclusive)', 'image': 'db.png' }, { 'url': '70efffaf86fe5bc089608d3cb297d3e276b9eb7a8f9f2fe6659c23a2d8b18edf', 'name': '1 Millionth Customer (Exclusive)', 'image': '1mil.png' }, { 'url': '2e002d5e1758e79ba51d08d92a0f3a95119f2f435ae7704916507b6c565a7da8', 'name': 'MrMessiah Cape (Exclusive)', 'image': 'mrm.png' }, { 'url': 'd8f8d13a1adf9636a16c31d47f3ecc9bb8d8533108aa5ad2a01b13b1a0c55eac', 'name': 'Prismarine Cape (Exclusive)', 'image': 'prismarine.png' }, { 'url': '5048ea61566353397247d2b7d946034de926b997d5e66c86483dfb1e031aee95', 'name': 'Turtle Cape (Exclusive)', 'image': 'turtle.png' } ]

def getMojangCape(name):
    site = requests.get(f"http://www.namemc.com/profile/{name}").text
    soup = BeautifulSoup(site, 'html.parser')

    container = soup.find_all("div", class_="card-body text-center")[1]

    capes = container.find_all("a")

    c = []
    for cape in capes:
        name = cape['title']

        c.append(name)

    out = []

    with open("./capes/capes.json", "r") as f:
        cFile = json.load(f)

    for i in c:
        for cape in cFile['capes']:
            if cape['name'] == i:
                out.append([i,cape['img']])
    
    return out


    url = f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}"

    x = requests.get(url)
    x = json.loads(x.text)
    
    decode = x['properties'][0]['value']
    x = json.loads(b64decode(decode))

    try:
        cape = x['textures']['CAPE']

    except:
        cape = None

    return cape

def getSkin(uuid):
    
    
    

    url = f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}"

    x = requests.get(url)
    x = json.loads(x.text)
    
    decode = x['properties'][0]['value']
    x = json.loads(b64decode(decode))

    try:
        skin = x['textures']['SKIN']

    except:
        skin = None

    return skin

