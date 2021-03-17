# Imports
import json


# Functions
def CreateJsonSingleplayer(Username):
    saveFile = {Username: {
        "username": Username,
        "health": 100,
        "damage": 5,
        "score": {
            "enemy_killed": 0,
            "time_played": 0,
            "total_score": 0
        },
        "inventory": {
            "potions": 2,
            "special_attacks": {
                "sp_attack_01": {
                    "name": "null",
                    "damage": 10
                },
                "sp_attack_02": {
                    "name": "null",
                    "damage": 10
                },
                "sp_attack_03": {
                    "name": "null",
                    "damage": 10
                },
            }
        }
    }}

    s = json.dumps(saveFile)

    with open("../saves/" + Username + "_savefile.json", "x") as f:
        f.write(s)


    print(saveFile)
    print(type(saveFile))


CreateJsonSingleplayer("Froggie")
