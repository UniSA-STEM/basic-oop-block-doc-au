"""
File: Rig.py
Description: Rig Class definition with attribute initialisation an methods - composition class used by Hacker and Asset.
Author: Neil John Cochrane
ID: 110484750
Username: COCNJ001
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Rig:

    # Initialisation of new rig - only name is passed in, other attributes with default settings
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = []
        self.__data_spikes = 2
        self.__removable_drive = 1
        self.__upgrade_level = 0

    # define __str__ for printout of rig specs...
    def __str__(self) -> str:
        demarcation_line = "=" * 30 + "\n"
        return_string = demarcation_line
        return_string += f"Rig name: {self.__name}\n"
        return_string += f"Condition: {self.current_condition()}\n"
        return_string += f"Upgrade level: {self.__upgrade_level}\n"
        return_string += f"Stored assets: {self.__storage}\n"
        return_string += demarcation_line
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

    def get_storage(self) -> list:
        return self.__storage

    def get_removable_drive(self) -> int:
        return self.__removable_drive

    def get_upgrade_level(self) -> int:
        return self.__upgrade_level


    # Setters...
    def set_name(self, name: str) -> None:
        if name is not None:
            self.__name = name

    def set_damage_counter(self, damage_counter: int) -> None:
        if damage_counter >= 0:
            self.__damage_counter = damage_counter

    def set_broken_state(self, broken_state: bool) -> None:
        self.__broken_state = broken_state

    def set_data_spikes(self, data_spikes: int) -> None:
        if data_spikes >= 0:
            self.__data_spikes = data_spikes

    def set_storage(self, item_to_add) -> list:
        if item_to_add is not None:
            self.__storage.append(item_to_add)

    def set_removable_drive(self, removable_drive) -> int:
        if removable_drive is not None:
            self.__removable_drive = removable_drive

    def set_upgrade_level(self, upgrade_level) -> int:
        if upgrade_level >= 0:
            self.__upgrade_level = upgrade_level


    # Set PROPERTIES for the class instance to allow dot notation calling externally
    name = property(get_name, set_name)
    damage_counter = property(get_damage_counter, set_damage_counter)
    broken_state = property(get_broken_state, set_broken_state)
    data_spikes = property(get_data_spikes, set_data_spikes)
    storage = property(get_storage, set_storage)
    removable_drive = property(get_removable_drive, set_removable_drive)
    upgrade_level = property(get_upgrade_level, set_upgrade_level)


    # FUNCTIONS for action pertaining to the rig..
    def current_condition(self) -> str:
        if self.__broken_state:
            condition = 0
        else:
            if self.__damage_counter == 0:
                condition = 2
            if self.__damage_counter == 1:
                condition = 1
            if self.__damage_counter == 2:
                condition = 0
        if condition == 0:
            return_string = "Broken (Level 0)"
        elif condition == 1:
            return_string = "Borderline (Level 1)"
        else:
            return_string = "Pristine (Level 2)"
        return return_string


    def repaired(self):
        print(f'Attempting to repair rig {self.name}...')
        if (self.__broken_state == True or self.__damage_counter > 0):
            self.set_broken_state(False)
            self.damage_counter = 0
            print(f"Repairs were completed on {self.name}")
            return True
        else:
            print(f"No repair is needed for rig {self.name}.")
            return False

    def upgrade(self, asset):
        self.__upgrade_level += 1

    def take_hit(self, asset):
        pass

    def generate_asset(self):
        pass

    def store_asset(self, asset):
        self.__storage.append(asset)

    def release_asset(self, asset):
        if asset is not None:
            if asset in self.__storage:
                self.__storage.remove(asset)







