"""
File: Rig.py
Description: This module displays the rig(computer) class which has methods
that repairs rig, upgrade, and store/transfer assets.
Author: Kim Xuyen Huynh
ID: 110442620
Username: HUYKX001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset


class Rig:
    """
    Constructor for the class Rig with private attributes such as
    name, damage counter, broken state, storage, removable drive, and upgrade level.
    """

    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = [Asset("RemovableDrive", "Used for extraction!"),
                          Asset("DataSpike", "used in battles!"),
                          Asset("DataSpike", "used in battles!"), ]
        self.__removable_drive = 1
        self.__upgrade_level = 0

    # Getters for the private attributes.
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
        # Returns asset name when matched.
        for asset in self.__storage:
            if asset.get_name() == asset_name:
                return asset

    def take_hit(self):
        """
        function will return the number of damage applied to the rigs.
        """
        # Applies damage numbers to rigs.
        self.__damage_counter += 1
        print(f"{self.get_name()} has taken hit!\n")

        # Rig is broken based on different upgrade level.
        if self.__upgrade_level == 0:
            if self.get_name() and self.__damage_counter == 2:
                self.__broken_state = True
                print(f"{self.get_name()} is now broken!\n")
        elif self.__upgrade_level == 1:
            if self.get_name() and self.__damage_counter == 3:
                self.__broken_state = True
                print(f"{self.get_name()} is now broken!\n")
        elif self.__upgrade_level == 3:
            if self.get_name() and self.__damage_counter == 4:
                self.__broken_state = True
                print(f"{self.get_name()} is now broken!\n")

    def repair_rig(self):
        """
        function sets repairs rig by setting broken state back to zero.
        """
        # Checks if rig is broken.
        if self.__broken_state:
            # Repairs the Rig broken state.
            self.__damage_counter = 0
            self.__broken_state = False
            print(f"{self.get_name()} has been repaired!\n")

    def state(self):
        """
        Returns the condition depending on the state of the rig.
        """
        if self.__broken_state:
            return f"Rig is in a broken state!"
        elif self.__damage_counter == 1:
            return f"Rig has been deteriorated"
        else:
            return f"Rig is in perfect condition!"

    def upgrade_rig(self, hacker):
        """
        Upgrades the rigs which range from level 1, 3. The rig can take on more attacks.
        """
        for assets in hacker.get_inventory():
            if isinstance(assets, Asset) and assets.get_name() == "HardwarePatch":
                # Upgrades the rig's level.
                if self.__upgrade_level < 3:
                    # increases the upgrade level
                    self.__upgrade_level += 1
                    print(f"{self.__name} has been upgraded to level ({self.__upgrade_level})\n")
                elif self.__upgrade_level <= 4:
                    # cannot upgrade to level 4
                    print(f"{self.__name} is at maximum capacity!\n")
                    # no hardware patch in inventory
                else:
                    print(f"{self.__name} does not have a hardware patch!")

    def store_release_assets(self, hacker, asset_name):
        """
        function gets the asset name, remove it from storage and transfer it to the inventory.
        """
        if hacker.encrypt_assets() is False:
            for assets in self.__storage:
                if assets.get_name() == asset_name:
                    # Removes assets from storage.
                    self.__storage.remove(assets)
                    # Adds the assets from storage into inventory.
                    hacker.get_inventory().append(assets)
                    print(f"removed {asset_name} and add it into {hacker.get_name()} inventory\n")
        else:
            print("Cannot transfer because encrypted!\n")

    def __str__(self):
        """
        returns the formatted information of Rig.
        """
        stored_asset = [asset.get_name() for asset in self.__storage]

        return (f"name: {self.__name}\n"
                f"condition: {self.state()}\n"
                f"upgrade level: {self.__upgrade_level}\n"
                f"stored assets: {", ".join(stored_asset)}\n")
