import sqlite3

def getEmbedColour(id):
    conn = sqlite3.connect("./data/guildSettings.db")

    curr = conn.cursor()
    sql = f'''SELECT * FROM Guild 
                WHERE ID=?'''
            
    args = (id,)
    curr.execute(sql, args)
    colour = int(curr.fetchone()[2])

    return colour

hypixelLogo = "https://hypixel.net/styles/hypixel-v2/images/header-logo.png"
mojangLogo = "https://www.minecraft.net/content/dam/franchise/logos/Mojang-Studios-Logo-Redbox.png"
optifineLogo = "https://pbs.twimg.com/profile_images/1134017073254813696/mKKb4k4N_400x400.png"
labyLogo = "https://www.labymod.net/page/tpl/assets/images/logo_web.png"
zigLogo = "https://avatars3.githubusercontent.com/u/51272906?s=200&v=4"
dinoLogo = "https://camo.githubusercontent.com/dc73478e13735d6fff8f2281863ff92399a3a9e7/68747470733a2f2f692e696d6775722e636f6d2f74356a326845312e706e67"