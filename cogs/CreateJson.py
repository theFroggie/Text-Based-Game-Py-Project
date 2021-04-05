# Imports
import json


# Functions
def CreateJsonSingleplayer(Username1):
    saveFileSolo = {Username1: {
        "username1": Username1,
        "health1": 100,
        "damage1": 5,
        "score1": {
            "enemy_killed": 0,
            "time_played": 0,
            "total_score": 0
        },
        "inventory1": {
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

    s = json.dumps(saveFileSolo)

    with open("./saves/singleplayer/" + Username1 + "_savefile.json", "x") as f:
        f.write(s)
        f.close()


def CreateJsonCoop(Username1, Username2):
    saveFileCoop = {Username1: {
        "username1": Username1,
        "health1": 100,
        "damage1": 5,
        "score1": {
            "enemy_killed": 0,
            "time_played": 0,
            "total_score": 0
        },
        "inventory1": {
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
        },
        "username2": Username2,
        "health2": 100,
        "damage2": 5,
        "score2": {
            "enemy_killed": 0,
            "time_played": 0,
            "total_score": 0
        },
        "inventory2": {
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

    s = json.dumps(saveFileCoop)

    with open("./saves/multiplayer/" + Username1 + "_savefile.json", "x") as f:
        f.write(s)
        f.close()


if __name__ == "__main__":
    CreateJsonSingleplayer()
    CreateJsonCoop()
