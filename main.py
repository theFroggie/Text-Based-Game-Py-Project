# Imports
from cogs import NewGame, LoadGame
import os

# Variables
Is_Singleplayer = False


# Functions
def Start():
    # Ask if they either want to play in single player or in co-op.
    Ask_Gametype = input("Do you want to play in Singleplayer or in Co-op? (s/c): ")

    # If the player input s (singleplayer), turns the bool Is_Singleplayer to True.
    if str(Ask_Gametype) == "s":
        Is_Singleplayer = True
    # If the player input c (co-op), turns the bool Is_Singleplayer to False.
    elif str(Ask_Gametype) == "c":
        Is_Singleplayer = False
    # If the player input nor c or s, restart the function.
    else:
        Start()

    # Ask if they either want to load a save or start a new game.
    Ask_LoadOrNew = input("Do you want to create a new game or load a save state? (n/l): ")

    # If the player input m (new game), turns the bool Is_New to True, clear the console and boot the NewGame file.
    if str(Ask_LoadOrNew) == "n":
        Is_New = True
        os.system("cls")
        NewGame.NewGame()
    # If the player input l (load save), turns the bool Is_New to False, clear the console and boot the NewGame file.
    elif str(Ask_LoadOrNew) == "l":
        Is_New = False
        os.system("cls")
        LoadGame.LoadGame()
    # If the player input nor n or l, restart the function.
    else:
        Start()


def SendBool(Newbool):
    Newbool = Is_Singleplayer

# Starts the function.
Start()
