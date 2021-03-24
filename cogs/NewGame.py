# Imports
import os
from cogs import CreateJson


def NewGameFunc(Is_Singleplayer):
    # Variables
    Carry_On = True

    while Carry_On:

        # Start procedure if in singleplayer.
        if Is_Singleplayer:

            Ask_Username1 = input("What is your name player? ")
            print(Ask_Username1)

            Confirm_Username = input(
                "confirm that '" + Ask_Username1 + "' is your username, you cannot change it. (y/n) ")

            if Confirm_Username == "y":
                # register save file with first username and register it in it.
                print("Creating save file with name `" + Ask_Username1 + "_savefile.json`")
                Carry_On = False
                CreateJson.CreateJsonSingleplayer(Ask_Username1)

            elif Confirm_Username == "n":
                # Send back at the start of the function.
                os.system("cls")
                continue

        # Start procedure if in co-op.
        elif not Is_Singleplayer:
            Ask_Username1 = input("What is your name player 1? ")
            print(Ask_Username1)

            Ask_Username2 = input("What is your name player 2? ")
            print(Ask_Username2)

            Confirm_Username = input(
                "confirm that `" + Ask_Username1 + "` and `" + Ask_Username2 + "` are your usernames, "
                                                                               "you cannot change "
                                                                               "them. (y/n) ")

            if Confirm_Username == "y":
                # register save file with first username and register it in it.
                print("Creating save file with name `" + Ask_Username1 + "_savefile.json`")
                Carry_On = False
                CreateJson.CreateJsonCoop(Ask_Username1, Ask_Username2)

            elif Confirm_Username == "n":
                # Send back at the start of the function.
                os.system("cls")
                continue
