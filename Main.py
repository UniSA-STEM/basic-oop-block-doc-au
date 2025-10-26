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
import random





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
        hacker_list = [hacker_1, hacker_2, hacker_3, hacker_4, hacker_5]
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
        rig_list = [rig_1, rig_2, rig_3, rig_4, rig_5]
        print(rig_1)
        print(rig_2)
        print(rig_3)
        print(rig_4)
        print(rig_5)

        # Then instantiate assets
        asset_1 = Asset()
        asset_2 = Asset()
        asset_3 = Asset()
        asset_4 = Asset()
        asset_5 = Asset()
        asset_6 = Asset()
        asset_7 = Asset()
        asset_8 = Asset()
        asset_9 = Asset()
        asset_10 = Asset()
        asset_list = [asset_1, asset_2, asset_3, asset_4, asset_5, asset_6, asset_7, asset_8, asset_9, asset_10]
        # ... and make 30 assets, just for fun
        asset_list = asset_list * 3
        for asset in asset_list:
            print(asset, asset.name)

        # Then randomly encrypt assets
        for asset in asset_list:
            option = random.randint(1, 2)
            if option == 1:
                asset.encrypt()



        # Assign rigs to each hacker random number of times
        print("\nTEST...\nAcquiring rigs for hackers....\n")
        for hacker in hacker_list:
            random_rig_allocation = random.randint(1, 5)
            for i in range(random_rig_allocation):
                print(f"Hacker {hacker.name} attempting to acquire a rig...\n")
                hacker.acquire_rig()


        #randomnly assign 5 assets to each hacker's rig
        print("\nTest...\nRandomly assigning assets to hackers' inventory...\n")
        for hacker in hacker_list:
            for i in range(5):
                option = random.randint(0, 29)
                asset = asset_list[option]
                hacker.rig.storage.append(asset)

        # print out each hacker's rig's inventory
        print("\nPrinting out each hacker's inventory...\n")
        for hacker in hacker_list:
            print(f"{hacker.name} has...")
            for asset in hacker.rig.storage:
                print(asset)
            print("\n==========\n")

        # Simulating battles, in no specific order... 10 rounds..
        for i in range(10):
            print(f"\nBattle round {i + 1}...")
            for hacker in hacker_list:
                # boost the attacker's data spikes, for a meatier battle
                hacker.rig.data_spikes += 1
                opponent_index = random.randint(0, 4)
                opponent = hacker_list[opponent_index]
                if hacker != opponent:  # check we aren't battling ourself...
                   hacker.launch_data_spike(opponent.rig)

        # List the hackers whio are now exposed....
        print("\nThe EXPOSED hackers are now...\n")
        for hacker in hacker_list:
            if hacker.exposed == True:
                print(hacker.name)

        # Again, print out each hacker's inventory
        print("\nPrinting out each hacker's post-battle inventory...\n")
        for hacker in hacker_list:
            print(f"{hacker.name} has (in their rig)...")
            for asset in hacker.rig.storage:
                print(asset)
            print("==========\n")

        for hacker in hacker_list:
            print(f"{hacker.name} has (in their inventory...")
            for asset in hacker.inventory:
                print(asset)
            print("==========\n")
        # For each hacker, decrypt all their encrypted assets and confirm
        print("\nNow decrypting all assets...\n")
        for hacker in hacker_list:
            print(f"{hacker.name}...")
            for asset in hacker.inventory:

                name_exists = hasattr(asset, 'name')
                if not name_exists:
                    print(f"Asset: name... doesnt seemingly exist...")
                if asset.get_encrypted == True:
                    print(f"{asset.name} is encrypted...")
                    asset.decrypt()
                    print(f"{asset.name} now decrypted.")


        print("\nTESTING FINISHED......\n")

    elif play_option == "2":
        # will allow interactive play
        print("This COULD be implemented later for interactive play.\n")
    else:
        print("So long, and thanks for checking out my work!\n")
        keep_playing = False

