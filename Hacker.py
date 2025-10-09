"""
File: Hacker.py
Description: This module represents the hacker class and has methods
that allow the hacker to...
Author: Kim Xuyen Huynh
ID: 110442620
Username: HUYKX001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset


class Hacker:
    def __init__(self, name):
        # Constructor for the class Hacker to initialise the variables.
        self.__name = name
        self.__inventory = [Asset("CryptoToken", "A digital currency!")]
        self.__rig = None
        self.__trace_level = 0

    # Getters for private attributes.
    def get_name(self):
        return self.__name

    def get_inventory(self):
        return self.__inventory

    def get_rig(self):
        return self.__rig

    def get_trace_level(self):
        return self.__trace_level

    def acquire_rig(self):
        # Acquires a rig with CryptoToken
        pass

    # String conversation method display Hacker & inventory contents.
    def __str__(self):
        return (f"Hacker's name:{self.__name}"
                f"rig name:"
                f"trace level: {self.__trace_level}"
                f"inventory: {self.__inventory}")
