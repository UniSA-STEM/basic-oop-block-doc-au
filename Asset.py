"""
File: Asset.py
Description: <A brief description of this Python module is coming.>
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# IMPOPRT statements
import random


class Asset:

    # Initialisation of the asset...
    def __init__(self, name: int, description: str) -> None:
        self.__name = name
        self.__description = description
        self.__encrypted = False
        self.__consumed = False
        self.__type = self.assign_asset_type()

    # __str__ definition to allow printout of asset
    def __str__(self):
        return_string = "=" * 30
        return_string += f"<{self.__name}>:<{self.__description}>"
        if self.__encrypted:
            return_string += f" [Encrypted]"
        return return_string

    def assign_asset_type(self):
        chosen_type = random.choice(['Crypto Token', 'Data Spike', 'Removable Drive', 'Security Chip', 'Hardware Patch'])
        return chosen_type



