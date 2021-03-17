# Imports
import os
from cogs import StartGame
import json as js

# Variables
Is_Singleplayer = False


# Functions
def NewGame():
    # Start procedure if in singleplayer.
    if Is_Singleplayer == True:
        Ask_Username1 = input("What is your name player? ")
        print(Ask_Username1)
        Confirm_Username = input("confirm that '" + Ask_Username1 + "' is your username, you cannot change it. (y/n) ")

        if Confirm_Username == "y":
            # register save file with first username and register it in it.
            print("Creating save file with name `" + Ask_Username1 + "_savefile.json`")
            StartGame.StartGame()
        elif Confirm_Username == "n":
            # Send back at the start of the function.
            NewGame()
        else:
            NewGame()

    # Start procedure if in co-op.
    elif Is_Singleplayer == False:
        Ask_Username1 = input("What is your name player 1? ")
        print(Ask_Username1)
        Ask_Username2 = input("What is your name player 2? ")
        print(Ask_Username2)
        Confirm_Username = input("confirm that `" + Ask_Username1 + "` and `" + Ask_Username2 + "` are your usernames, "
                                                                                                "you cannot change "
                                                                                                "them. (y/n) ")

        if Confirm_Username == "y":
            # register save file with first username and register it in it.
            print("Creating save file with name `" + Ask_Username1 + "_savefile.json`")
            StartGame.StartGame()
        elif Confirm_Username == "n":
            # Send back at the start of the function.
            NewGame()
        else:
            NewGame()
