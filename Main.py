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





def old_tests():
    if new_hacker.rig == None:
        print(f'This hacker has no rig!\n')
        new_hacker.aquire_rig()
        print(f'Attempting to purchase a second rig..\n')
        new_hacker.aquire_rig()
    else:
        print('The rig already stored is..')
        print(new_hacker.rig)

    if new_hacker.rig == None:
        print(f'\nOn second check... this hacker has no rig!')
        new_hacker.aquire_rig()
        print(f'\nAttempting to purchase a second rig..')
        new_hacker.aquire_rig()
    else:
        print(f'\nOn second check... the rig already stored is..')
        print(new_hacker.rig)

    new_asset.encrypt()

    print(new_asset)

    new_hacker.repair_rig()

    new_hacker.crypto_token += 1
    new_hacker.repair_rig()
    new_hacker.rig.broken_state = True
    new_hacker.repair_rig()
    new_hacker.repair_rig()


# MAIN programme

print("Welcome to HackZone - where your digital dreams (or nightmares) come true!!\n")
keep_playing = True
while keep_playing:
    play_option = input("Press 1 to enter TEST suite, 2 to PLAY or *anything else* to EXIT : ")
    if play_option == "1":
        # testing mode

        # First, instantiate hackers
        hacker_1 = Hacker('DigitalMisery')
        hacker_2 = Hacker('LevelPlayingFieldz')
        hacker_3 = Hacker('HacksOnYou')
        hacker_4 = Hacker('CyberInsecurity')
        hacker_5 = Hacker('GiantKillas')
        print(hacker_1)
        print(hacker_2)
        print(hacker_3)
        print(hacker_4)
        print(hacker_5)

        # Then instantiate rigs
        rig_1 = Rig('1st Rig')
        rig_2 = Rig('2nd Rig')
        rig_3 = Rig('3rd Rig')
        rig_4 = Rig('4th Rig')
        rig_5 = Rig('5th Rig')
        print(rig_1)
        print(rig_2)
        print(rig_3)
        print(rig_4)
        print(rig_5)

        list_rigs()
        print("\nTesting finished......\n")
    elif play_option == "2":
        # will allow interactive play
        print("This COULD be implemented later for interactive play.\n")
    else:
        print("So long, and thanks for checking out my work!\n")
        keep_playing = False

