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

    def set_exposed(self, exposed: bool) -> None:
        self.__exposed = exposed

    def set_rig(self, rig: Rig) -> None:
        self.__rig = rig

    def set_crypto_token(self, token: int) -> None:
        if token is not None:
            self.__crypto_token = token

    # Properties
    name = property(get_name, set_name)
    inventory = property(get_inventory, set_inventory)
    rig = property(get_rig, set_rig)
    crypto_token = property(get_crypto_token, set_crypto_token)
    trace_level = property(get_trace_level)
    exposed = property(get_exposed, set_exposed)



    # Needed functions per spec...

    def launch_data_spike(self, other_rig):
        #Announce the attack
        print(f"{self.__name} is attacking {other_rig}...")
        # Check if there is a rig for the hacker
        if other_rig is not None:
            # Does my rig have a data spike?
            if self.__rig.data_spikes > 0:
                # As all good... launch the attack and consume a dataspike
                self.__trace_level += 1
                self.__rig.data_spikes -= 1
                other_rig.damage_counter += 1
                # Determine if can extract assets from damaged rig
                if other_rig.damage_counter == 0:
                    # Can now remove all unencrypted assets from other rig
                    self.extract_unsecured_assets(other_rig)
            else:
                print("The attack was unsuccessful!")
        else:
            print(f"The asset is a {asset.name} and not a Data Spike.  Can't be used as such.")

        if self.trace_level > 4:
            print(f"{self.name} now has a trace level of {self.trace_level} and is now EXPOSED !!")
            self.exposed = True

    def aquire_rig(self):
        if self.__exposed == False:
            if self.__crypto_token > 0:
                self.__rig = Rig('The Emperors New Rig')
                print('The Emperors New Rig has been aquired...')
                print(self.__rig)
                self.__crypto_token -= 1
            else:
                print('Sadly you have insufficient funds to purchase a rig!')
        else:
            print(f"{self.name} has  been exposed.  Can't do this at the moment.")

    def extract_unsecured_assets(self, other_rig):
        # Ensure not exposed and have a removable drive before preoceeding
        if self.__exposed == False:
            if self.rig.removable_drive > 0:
                # Check the attacked rig has assets to remove in it's inventory
                if len(other_rig.storage) > 0:
                    # sequentially check items in storage (other rig) for encryption status and transfer if not
                    extraction_count = 0
                    for item in other_rig.storage:
                        if item.encrypted == False:
                            self.__inventory.append(item)
                            other_rig.storage.remove(item)
                            extraction_count += 1
                    if extraction_count > 0: # have removed something...
                        self.__trace_level += 1
                        self.rig.removable_drive -= 1
            else:
                print(f"{self.name}'s rig does not have a removable drive, so cannot proceed.")
        else:
            print(f"{self.name} has  been exposed.  Can't do this at the moment.")

    def encrypt_asset(self, asset):
        if self.__exposed == False:
            has_security_chip = False
            if len(self.__inventory) > 0:
                for item in self.__inventory:
                    if item.name == 'Security Chip':
                        has_security_chip = True
            if has_security_chip:
                asset.encrypt()
        else:
            print(f"{self.name} has  been exposed.  Can't do this at the moment.")

    def decrypt_asset(self, asset):
        if self.__exposed == False:
            has_security_chip = False
            if len(self.__inventory) > 0:
                for item in self.__inventory:
                    if item.name == 'Security Chip':
                        has_security_chip = True
            if has_security_chip:
                asset.decrypt()
        else:
            print(f"{self.name} has  been exposed.  Can't do this at the moment.")

    def repair_rig(self):
        print(f'In Hacker class... about to repair check... have crypto of {self.crypto_token}...')
        if self.__crypto_token > 0:
            repairs_done = self.rig.repaired()
            if repairs_done:
                self.__crypto_token -= 1

    def upgrade_rig(self):
        # Need to have a rig to upgrade it, so check
        if self.__rig != None:
            # Need a Hardware Patch in inventory to upgrade, so check for same
            has_hardware_patch = False
            if len(self.__inventory) > 0:
                for item in self.__inventory:
                    if item.name == 'Hardware Patch':
                        has_hardware_patch = True
            if has_hardware_patch:
                self.__rig.upgraded = True

    def store_asset(self, asset):
        if asset is not None:
            self.__rig.storage.append(asset)
            self.inventory.remove(asset)

    def store_asset(self):
        for item in self.__inventory:
            self.__rig.storage.append(item)
            self.inventory.remove(item)

    def retrieve_asset(self, asset):
        if asset is not None:
            asset_transfer_count = 0
            for item in self.__rig.storage:
                if item == asset:
                    if asset_transfer_count < 1: # so only one /first asset is retrieved
                        self.inventory.append(asset)
                        self.__rig.storage.remove(asset)
                        asset_transfer_count += 1

    def retrieve_asset(self):
        for item in self.__rig.storage:
            self.inventory.append(item)
            self.__rig.storage.remove(item)


    def scan_inventory(self, asset_name):
        if asset_name is not None:
            asset_removal_count = 0
            for item in self.__inventory:
                if item.name == asset_name:
                    if asset_removal_count < 1:  # so only one /first asset is retrieved and removed
                        print(f"An asset '{item.name}' has been found in {self.__name}'s inventory and will now be removed.")
                        self.__inventory.remove(item)
                        asset_removal_count += 1


    def reduce_trace(self):
        print(f"{self.name} has done something nefarious to reduce their trace from {self.trace_level} to {self.__trace_level - 1} AND are no longer exposed...")
        self.__trace_level -= 1
        self.__exposed = False





