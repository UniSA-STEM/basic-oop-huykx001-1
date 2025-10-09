"""
File: Rig.py
Description: This module displays the rig(computer) class which has methods
that...
Author: Kim Xuyen Huynh
ID: 110442620
Username: HUYKX001
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Rig:
    def __init__(self, name):
        # Constructor for the class Rig to initialise the variables.
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = []
        self.__data_spikes = 2
        self.__removable_drive = 1
        self.__upgrade_level = 0

    # String conversation method to format Rig.
    def __str__(self):
        pass
