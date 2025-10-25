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

# MAIN programme



#temp code for checking purposes only
new_hacker = Hacker('DigitalMisery')
new_asset = Asset()
new_rig = Rig('First External Rig')

print(new_hacker)
print(new_asset)
print(new_rig)

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


