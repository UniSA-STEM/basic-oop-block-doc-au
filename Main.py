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
    new_hacker.repair_rig()

    new_hacker.crypto_token += 1
    new_hacker.repair_rig()
    new_hacker.rig.broken_state = True
    new_hacker.repair_rig()
    new_hacker.repair_rig()


# MAIN programme
"""
This is the MAIN programme start point, utlising imports from Asset, Rig and
Hacker classes.
Although not implemented, there is option for adding a module that allow a 'game'
whereby the user could chose actions from a menu and play with as many characters
etc. and for as long as enjoyable.
"""

print("===========================================================================\n")
print("Welcome to HackZone - where your digital dreams (or nightmares) come true!!\n")
print("===========================================================================\n")

# Loop through the (basic) menu until a cancel code entered
keep_playing = True
while keep_playing:
    play_option = input("Press 1 to enter TEST suite, 2 to PLAY or *anything else* to EXIT : ")
    if play_option == "1":
        # testing mode
        print("\n\nTESTING SUITE...\n")
        # First, instantiate hackers
        print("First, we will instantiate 5 hackers...\n")
        hacker_1 = Hacker('DigitalMisery')
        hacker_2 = Hacker('LevelPlayingFieldz')
        hacker_3 = Hacker('HacksOnYou')
        hacker_4 = Hacker('CyberInsecurity')
        hacker_5 = Hacker('GiantKillas')
        # Create a lst of hackers for later test loops of all
        hacker_list = [hacker_1, hacker_2, hacker_3, hacker_4, hacker_5]
        for hacker in hacker_list:
            print(hacker)


        # Then instantiate rigs
        print("Next, we will instantiate 5 rigs...\n")
        rig_1 = Rig('1st Rig')
        rig_2 = Rig('2nd Rig')
        rig_3 = Rig('3rd Rig')
        rig_4 = Rig('4th Rig')
        rig_5 = Rig('5th Rig')
        # Create a lst of rigs for later test-loops of all
        rig_list = [rig_1, rig_2, rig_3, rig_4, rig_5]
        for rig in rig_list:
            print(rig)


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
        # ... and multiply to make 30 assets, just for fun
        asset_list = asset_list * 3
        print("These are all the instantiated assets...\n")
        for asset in asset_list:
            print(asset)

        # Then randomly encrypt assets
        for asset in asset_list:
            option = random.randint(1, 10)
            if option < 6 :
                asset.encrypt()
            else:
                asset.decrypt()

        # Try and upgrade a hacker without a rig
        print(f"\n\n{hacker_1.name} is trying to upgrade their rig (without one)...")
        hacker_1.upgrade_rig()

        # Assign rigs to each hacker random number of times
        print("\nThirdly... Acquiring rigs for hackers....\n")
        for hacker in hacker_list:
            random_rig_allocation = random.randint(1, 5)
            for i in range(random_rig_allocation):
                print(f"Hacker {hacker.name} attempting to acquire a rig...\n")
                hacker.acquire_rig()

        # Have another go at upgrading a rig...
        print(f"{hacker_1.name} again trying to upgrade their rig...")
        hacker_1.upgrade_rig()

        #OK... so add a hardware patch and re-try upgrade
        print(f"\n{hacker_1.name} again trying to upgrade their rig (after getting a hardware patch)...")
        patch_count = 0
        for asset in asset_list:
            if asset.name == 'Hardware Patch':
                if patch_count < 1:
                    hacker_1.inventory.append(asset)
                    patch_count +=1
        hacker_1.upgrade_rig()
        print(hacker_1.rig)

        #randomnly assign 5 assets to each hacker's inventory
        print("\nACTION...\nRandomly assigning 5 assets of the 30 to hackers' inventory ...\n")
        for hacker in hacker_list:
            for i in range(5):
                option = random.randint(0, 29)
                asset = asset_list[option]
                hacker.inventory.append(asset)


        # print out each hacker's rig's inventory
        print("\nPrinting out each hacker's rig storage list (should still be empty)...\n")
        for hacker in hacker_list:
            print(f"{hacker.name} has...")
            for asset in hacker.rig.storage:
                print(asset)
            print("\n==========\n")

        # randomnly assign 5 assets to each hacker's rig's storage
        print("\nACTION...\nRandomly assigning 5 assets of the 30 to hackers' rig's storage ...\n")
        for hacker in hacker_list:
            for i in range(5):
                option = random.randint(0, 29)
                asset = asset_list[option]
                hacker.rig.storage.append(asset)

        # print out each hacker's rig's inventory
        print("\nPrinting out each hacker's rig storage list (should still be empty)...\n")
        for hacker in hacker_list:
            print(f"{hacker.name} has...")
            for asset in hacker.rig.storage:
                print(asset)
            print("\n==========\n")

        # print out each hacker's  inventory
        print("\nAnd printing out each hacker's own inventory...\n")
        for hacker in hacker_list:
            print(f"{hacker.name} has...")
            for asset in hacker.inventory:
                print(asset)
            print(f"Total assets in inventory : {len(hacker.inventory)}")
            print("\n==========\n")

        # Simulating BATTLES, in no specific order... 10 rounds..
        print("\n\nBATTLE STATIONS...\n\n")
        for i in range(10):
            print(f"\nBattle round {i + 1}...")
            for hacker in hacker_list:
                # boost the attacker's data spikes, for a meatier battle
                hacker.rig.data_spikes += 1
                opponent_index = random.randint(0, 4)
                opponent = hacker_list[opponent_index]
                if hacker != opponent:  # check we aren't battling ourself...
                   hacker.launch_data_spike(opponent.rig)
            # randomly repair some rigs at round 5
            if i == 4:
                print("\nResetting a few trace levels now...\n\n")
                for hacker in hacker_list:
                    repair_option = random.randint(1, 10)
                    if repair_option > 5:
                        hacker.repair_rig()
                        hacker.trace_level = 0
                        hacker.exposed = False

        # List the hackers whio are now exposed....
        print("\nThe EXPOSED hackers are now...\n")
        for hacker in hacker_list:
            if hacker.exposed == True:
                print(hacker.name)

        # Upgrade some rigs, randomly...
        for hacker in hacker_list:
            chose_upgrade = random.randint(1, 10)
            if chose_upgrade > 5:
                hacker.rig.upgrade()
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
        print("\nNow decrypting all assets on rigs...\n")
        for hacker in hacker_list:
            print(f"{hacker.name}...")
            for asset in hacker.rig.storage:
                asset.decrypt()
        print("\n ****** Now to check all items were indeed decrypted...")
        for hacker in hacker_list:
            print(f"\n{hacker.name}...")
            for asset in hacker.rig.storage:
                print(asset)

        # now use Hacker_1 to attack all others and steel all their rig's items..
        print(f"\n\n\n{hacker_1.name} will now attack the remining hackers !! \n")
        hacker_1.exposed = False
        hacker_1.rig.removable_drive = 5
        print(f"{hacker_1.name}'s removable drive count is {hacker_1.rig.removable_drive}.")
        for hacker_number in range(1, 5):
            hacker_list[hacker_number].exposed = True
            hacker_list[hacker_number].rig.removable_drive = 1
            print(f"Snooping into rig of {hacker_list[hacker_number].name}...\n")
            for item in hacker_list[hacker_number].rig.storage:
                hacker_1.extract_unsecured_assets(hacker_list[hacker_number].rig)
        print("\n\nPrinting out the post-robbery inventory...\n")
        for hacker in hacker_list:
            print(f"{hacker.name} has (in their inventory)...")
            for asset in hacker.inventory:
                print(asset)
            print("==========\n")
        for hacker in hacker_list:
            print(f"And just for comparison, {hacker.name} has (in their rig's storage)...")
            for asset in hacker.rig.storage:
                print(asset)
            print("==========\n")


        # Print trace levels for ech hacker..
        print("Now printing the trace level for each hacker...\n")
        for hacker in hacker_list:
            print(f"For {hacker.name} the current trace level is {hacker.trace_level}")
        print("\nSo let's reduce those a tad...")
        for hacker in hacker_list:
            hacker.reduce_trace()
        print("\nNow printing the NEW trace level for each hacker...\n")
        for hacker in hacker_list:
            print(f"For {hacker.name} the NEW trace level is {hacker.trace_level}")


        # Now encrypt all inventory items
        print("Will re-encrypt all inventory items...")
        for hacker in hacker_list:
            for asset in hacker.inventory:
                asset.encrypt()
        print("\nNow to check all inventory items were indeed encrypted...")
        for hacker in hacker_list:
            print(f"\n{hacker.name}...")
            for asset in hacker.inventory:
                print(asset)

        print("\n\nTESTING FINISHED......\n")

    elif play_option == "2":
        # will allow interactive play
        print("This COULD be implemented later for interactive play.\n")
    else:
        print("\n\nSo long, and thanks for checking out my work!\n")
        keep_playing = False

