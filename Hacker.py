"""
File: Hacker.py
Description: This module creates the Hacker class and related (encapsulated) functions.
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# IMPORT statements
from Rig import Rig
from Asset import Asset

#CLASS definition and methods
class Hacker:

    # initialisation attributes go here
    def __init__(self, name: str)  -> None:
        self.__name = name
        self.__inventory = []
        self.__rig = None
        self.__crypto_token = 1
        self.__trace_level = 0
        self.__exposed = False

    # __str__ definition for print ing of object...

    def __str__(self) -> str:
        return_string = f"\nHacker name: {self.__name}\n"
        return_string += f"Hacker's trace level: {self.__trace_level}\n"
        return_string += f"Hacker's inventory: {self.__inventory}\n"
        return return_string

    # Needed MODIFIERS for this object - basic at this stage
    #GETTERS
    def get_name(self) -> str:
        return self.__name

    def get_inventory(self) -> list:
        return self.__inventory

    def get_rig(self) -> object:
        return self.__rig

    def get_crypto_token(self) -> int:
        return self.__crypto_token

    def get_trace_level(self) -> int:
        return self.__trace_level

    def get_exposed(self) -> bool:
        return self.__exposed

    # SETTERS .. at this stage others are only modified by internal functions
    def set_name(self, name: str) -> None:
        if name is not None:
            self.__name = name

    def set_inventory(self, inventory: list) -> None:
        self.__inventory = inventory

    # Properties
    name = property(get_name, set_name)
    inventory = property(get_inventory, set_inventory)
    rig = property(get_rig)
    crypto_token = property(get_crypto_token)
    trace_level = property(get_trace_level)
    exposed = property(get_exposed)



    # Need functions per spec... TBC

    def launch_data_attack(self, asset, other_rig):
        #Announcve the attack
        print(f"{self.__name} is attacking {other_rig} with {asset}...")
        # Check if the asset is a data spike
        if asset.name == 'Data Spike':
            # Check if there is a rig for the hacker
            if other_rig is not None:
                # If there is a rig, does it have a data spike?
                if self.rig.data_spikes > 0:
                    # If all good... launch the attack and consume a dataspike
                    self.__trace_level += 1
                    self.rig.data_spikes -= 1
                    other_rig.damage_counter += 1
                else:
                    print("The attack was unsuccessful!")
        else:
            print(f"The asset is a {asset.name} and not a Data Spike.  Can't be used as such.")

    def aquire_rig(self):
        if self.__crypto_token > 0:
            self.__rig = Rig('The Emperors New Rig')
            print('The Emperors New Rig has been aquired...')
            print(self.__rig)
            self.__crypto_token -= 1
        else:
            print('Sadly you have insufficient funds to purchase a rig!')

    def extract_assets(self, asset):
        pass

    def encrypt_asset(self, asset):
        pass

    def upgrade_rig(self, rig):
        pass

    def store_asset(self, asset, rig):
        pass

    def retrieve_asset(self, asset, rig):
        pass

    def scan_inventory(self, asset):
        pass






