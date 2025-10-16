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
        self.__storage = [Asset("RemovableDrive", "Used for extraction!")]
        self.__data_spikes = 2
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

    def get_data_spikes(self):
        return self.__data_spikes

    def get_removable_drive(self):
        return self.__removable_drive

    def get_upgrade_level(self):
        return self.__upgrade_level

    # String conversation method to format Rig.
    def __str__(self):
        pass
