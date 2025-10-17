"""
File: Rig.py
Description: This module displays the rig(computer) class which has methods
that...
Author: Kim Xuyen Huynh
ID: 110442620
Username: HUYKX001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset


class Rig:
    def __init__(self, name):
        # Constructor for the class Rig to initialise the variables.
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = [Asset("RemovableDrive", "Used for extraction!"),
                          Asset("DataSpike", "used in battles!"),
                          Asset("DataSpike", "used in battles!")]
        self.__removable_drive = 1
        self.__upgrade_level = 0

    # Getters for the private attribute
    def get_name(self):
        return self.__name

    def get_damage_counter(self):
        return self.__damage_counter

    def get_broken_state(self):
        return self.__broken_state

    def get_storage(self):
        return self.__storage

    def get_removable_drive(self):
        return self.__removable_drive

    def get_upgrade_level(self):
        return self.__upgrade_level

    def asset_name_retrieve(self, asset_name):
        # returns asset name when matched
        for asset in self.__storage:
            if asset.get_name() == asset_name:
                return asset

    def take_hit(self):
        # applies damage numbers to rigs
        self.__damage_counter += 1
        print(f"{self.get_name()} has taken hit!")

        # Rig is now broken after 2 hits
        if self.get_name() and self.__damage_counter == 2:
            self.__broken_state = True
            print(f"{self.get_name()} is now broken!")

    def repair_rig(self):
        # checks if rig is broke
        if self.__broken_state:
            # repairs the Rig broken state
            self.__damage_counter = 0
            self.__broken_state = False
            print(f"{self.get_name()} has been repaired!")

    # String conversation method to format Rig.
    def __str__(self):
        pass
