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

    # define __str__ for printout of rig specs...
    def __str__(self):
        return_string = "=" * 30 + "\n"
        return_string += f"Rig name: {self.__name}\n"
        return_string += f"Condition: {self.current_condition()}\n"
        return_string += f"Upgrade level: {self.__upgrade_level}\n"
        return_string += f"Stored assets: {self.__storage}\n"
        return_string += "=" * 30 + "\n"
        return return_string

    # MODIFIER definitions
    # Getters...
    def get_name(self) -> str:
        return self.__name

    def get_damage_counter(self) -> int:
        return self.__damage_counter

    def get_data_spikes(self) -> int:
        return self.__data_spikes

    def get_broken_state(self) -> bool:
        return self.__broken_state

    # Setters...
    def set_name(self, name: str) -> None:
        if name is not None:
            self.__name = name

    def set_damage_counter(self, damage_counter: int) -> None:
        if damage_counter >0:
            self.__damage_counter = damage_counter

    def set_broken_state(self, broken_state: bool) -> None:
        self.__broken_state = broken_state

    def set_data_spikes(self, data_spikes: int) -> None:
        if data_spikes > 0:
            self.__data_spikes = data_spikes

    # Set PROPERTIES for the class instance
    name = property(get_name, set_name)
    damage_counter = property(get_damage_counter, set_damage_counter)
    broken_state = property(get_broken_state, set_broken_state)
    data_spikes = property(get_data_spikes, set_data_spikes)

    # FUNCTIONS for action pertaining to the rig..
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






