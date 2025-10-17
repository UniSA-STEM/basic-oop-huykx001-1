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
        self.__rig_count = 0  # checks amount of Rigs

    # Getters for private attributes.
    def get_name(self):
        return self.__name

    def get_inventory(self):
        return self.__inventory

    def get_rig(self):
        return self.__rig

    def get_trace_level(self):
        return self.__trace_level

    def get_rig_count(self):
        return self.__rig_count

    # Note: might keep later or not.
    def check_rig(self):
        if self.__rig_count != 0 and self.__rig_count < 0:
            return False
        else:
            return True

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
            self.__rig_count += 1
            print(f"{self.__name} has activated the rig :)")
        else:
            print(f"{self.__name} does not enough CryptoToken to acquire a rig!")

    # TODO: Create a way to remove data spike from storage
    def launch_data_spikes(self, foe_rig):
        # checks that trace levels don't exceed past 5
        if self.__trace_level != 5:
            # Checks if hacker has a rig
            if self.check_rig():
                if foe_rig.get_damage_counter() < 2:
                    if self.__rig.asset_name_retrieve("DataSpike"):
                        foe_rig.take_hit()
                        # hacker trace level increases
                        self.__trace_level += 1
                else:
                    print(f"{self.__name} does not have any data spikes :(")
        else:
            print(f"{self.__name} is too exposed! reduce the traces!")

    # String conversion method display Hacker & inventory contents.
    # def __str__(self):
    #     return (f"Hacker's name:{self.__name}\n"
    #             f"rig name:{self.__rig.get_name()}\n"
    #             f"trace level: {self.__trace_level}\n"
    #             f"inventory: {self.__inventory}\n")
