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
        # stores assets
        self.__inventory = [Asset("CryptoToken", "A digital currency!"),
                            Asset("SecurityChip", "Encrypts or decrypts assets!"),
                            Asset("HardwarePatch", "Upgrade rigs!")]
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

    def check_rig(self):
        if self.__rig != None:
            return True
        else:
            return False

    def retrieve_asset_name(self, asset_name):
        # returns the asset when name is matched.
        for asset in self.__inventory:
            if asset.get_name() == asset_name:
                return asset

    def acquire_rig(self, rig):
        # Acquires a rig with CryptoToken
        if self.retrieve_asset_name("CryptoToken"):
            # removes CryptoToken from inventory
            self.__inventory.remove(self.retrieve_asset_name("CryptoToken"))
            # acquired a rig
            self.__rig = rig
            print(f"{self.__name} has activated the rig :)")
        else:
            print(f"{self.__name} does not enough CryptoToken to acquire a rig!")

    def launch_data_spikes(self, foe_rig):
        # Checks if hacker has a rig
        if self.check_rig():
            if foe_rig.get_damage_counter() < 2:
                if self.retrieve_asset_name("DataSpike"):
                    foe_rig.take_hit()
            else:
                print(f"{self.__name} does not have any data spikes :(")

    # String conversion method display Hacker & inventory contents.
    # def __str__(self):
    #     return (f"Hacker's name:{self.__name}\n"
    #             f"rig name:{self.__rig.get_name()}\n"
    #             f"trace level: {self.__trace_level}\n"
    #             f"inventory: {self.__inventory}\n")
