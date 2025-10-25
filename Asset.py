"""
File: Asset.py
Description: <A brief description of this Python module is coming.>
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# IMPORT statements
import random


class Asset:

    # Initialisation of the asset...
    def __init__(self) -> None:
        self.__name = self.assign_asset_type()
        # print(f'In asset name instantiation... name given as {self.__name}')
        self.__description = self.assign_asset_description()
        self.__encrypted = False
        self.__consumed = False
        # self.__type = self.assign_asset_type()

    # __str__ definition to allow printout of asset
    def __str__(self):
        return_string = f"<{self.__name}>:<{self.__description}>"
        if self.__encrypted:
            return_string += f"[Encrypted]"
        return return_string

    # MODIFIERS for this class
    # Getters...
    def get_description(self):
        return {self.__description}

    def get_encrypted(self):
        return self.__encrypted

    def get_consumed(self):
        return self.__consumed

    # Setters...
    def set_description(self, description):
        if description is not None:
            self.__description = description

    def set_encrypted(self, encryption) -> bool:
        self.__encrypted = encryption

    def set_consumed(self, consumed) -> bool:
        if consumed is not None:
            self.__consumed = consumed


    # PROPERTIES to allow external access
        description = property(get_description, set_description)
        encrypted = property(get_encrypted, set_encrypted)
        consumed = property(get_consumed,set_consumed)



    def assign_asset_type(self):
        chosen_type = random.choice(['Crypto Token', 'Data Spike', 'Removable Drive', 'Security Chip', 'Hardware Patch'])
        return chosen_type

    #On instantiation, a description will be made which fits the assets name (type)
    def assign_asset_description(self):
        # print(f'In asset class def... asset name passed-in as {self.__name}')
        if self.__name == 'Crypto Token':
            description = "This is a crypto-token, used to acquire or repair rigs."
        if self.__name == 'Data Spike':
            description = "This is a data spike, used in battles and the cause of great damage!"
        if self.__name == 'Removable Drive':
            description = "This is a removable drive, found in rigs and used for extraction purposes."
        if self.__name == 'Security Chip':
            description = "This is a security chip, used to encrypt or decrypt assets."
        if self.__name == 'Hardware Patch':
            description = "This is a hardware patch, used to upgrade rigs."
        # print(f'At end of description def, the name is {self.__name} and the definiton is {description}')
        return description

    def encrypt(self):
        self.__encrypted = True

    def decrypt(self):
        self.__encrypted = False

