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
new_hacker = Hacker('DastardlyBob')
new_asset = Asset()
#new_rig = Rig('FirstRig')

if new_hacker.rig == None:
    print('This hacker has no rig!')
    new_hacker.aquire_rig()
    print('Attempting to purchase a second rig..')
    new_hacker.aquire_rig()
else:
    print('The rig already stored is..')
    print(new_hacker.rig)

if new_hacker.rig == None:
    print('On second check... this hacker has no rig!')
    new_hacker.aquire_rig()
    print('Attempting to purchase a second rig..')
    new_hacker.aquire_rig()
else:
    print('On second check... the rig already stored is..')
    print(new_hacker.rig)

print(new_hacker)
print(new_asset)
#print(new_rig)
new_asset.encrypt()

print(new_asset)

