"""
File: main.py
Description: This module will import relevant classes to allow testing and interaction between hacker, rig and asset objects per spec's.
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# IMPORT statements, to allow class access

from Asset import Asset
from Hacker import Hacker
from Rig import Rig
import Tests


# MAIN programme

print("Welcome to HackZone - where your digital dreams (or nightmares) come true!!\n")
keep_playing = True
while keep_playing:
    play_option = input("Press 1 to enter TEST suite, 2 to PLAY or *anything else* to EXIT : ")
    if play_option == "1":
        # testing mode
        Tests.testing()
    elif play_option == "2":
        # will allow interactive play
        print("This will be implemented later for interactive play.\n")
    else:
        print("So long, and thanks for checking out my work!\n")
        keep_playing = False

