"""
File: Hacker.py
Description: <A brief description of this Python module is coming.>
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""


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
        return_string = f"Hacker name: {self.__name}\n"
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


# Need functions per spec... TBC

    def launch_data_attack(self, rig):
        pass

    def aquire_rig(self, rig):
        pass

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






