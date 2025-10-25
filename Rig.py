"""
File: Rig.py
Description: <A brief description of this Python module is coming.>
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Rig:

    # Initialisation of new rig
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = []
        self.__data_spikes = 2
        self.__removable_drive = 1
        self.__upgrade_level = 0

    # define __str__ for prinout of rig sepcs...
    def __str__(self):
        return_string = "=" * 30
        return_string += f"Rig name: {self.__name}\n"
        return_string += f"Condition: {self.current_condition()}\n"
        return_string += f"Upgrade level: {self.__upgrade_level}\n"
        return_string += f"Stored assets: {self.__storage}\n"
        return_string += "=" * 30
        return return_string


    def current_condition(self):
        pass

    def repaired(self, crypto_token):
        pass

    def upgraded(self, asset):
        pass

    def take_hit(self, asset):
        pass

    def generate_asset(self):
        pass

    def store_asset(self, asset):
        pass

    def release_asset(self, asset):
        pass






