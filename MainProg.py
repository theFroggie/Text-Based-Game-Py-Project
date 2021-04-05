# Imports
import os
from cogs import NewGame, LoadGame


# Functions
def StartFunc():
    # Variables
    Is_Singleplayer = False
    Carry_On_1 = True
    Carry_On_2 = True

    # Will loop until the choice is made
    while Carry_On_1:
        # Ask if they either want to play in single player or in co-op.
        Ask_Gametype = input("Do you want to play in Singleplayer or in Co-op? (s/c): ")

        # If the player input s (singleplayer), turns the bool Is_Singleplayer to True.
        if Ask_Gametype == "s":
            Is_Singleplayer = True
            Carry_On_1 = False

        # If the player input c (co-op), turns the bool Is_Singleplayer to False.
        elif Ask_Gametype == "c":
            Is_Singleplayer = False
            Carry_On_1 = False

    # Will loop until the choice is made
    while Carry_On_2:
        # Ask if they either want to load a save or start a new game.
        Ask_LoadOrNew = input("Do you want to create a new game or load a save state? (n/l): ")

        # If the player input m (new game), turns the bool Is_New to True, clear the console and boot the NewGame file.
        if Ask_LoadOrNew == "n":
            Carry_On_2 = False
            os.system("cls")
            NewGame.NewGameFunc(Is_Singleplayer)

        # If the player input l (load save), turns the bool Is_New to False, clear the console and boot the NewGame
        # file.
        elif Ask_LoadOrNew == "l":
            Carry_On_2 = False
            os.system("cls")
            LoadGame.LoadGameFunc()

    # Return the Is_Singleplayer for NewGame
    return Is_Singleplayer


# Starts the function.
if __name__ == "__main__":
    StartFunc()
