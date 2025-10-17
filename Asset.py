"""
File: Asset.py
Description: This module displays the asset class which does a string conversion
that displays the name and description.
Author: Kim Xuyen Huynh
ID: 110442620
Username: HUYKX001
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    def __init__(self, name, description):
        # Constructor for the class Asset to initialise the variables.
        self.__name = name
        self.__description = description
        self.__encrypted = None

    # Getter for name private attribute.
    def get_name(self):
        return self.__name

    def get_encrypted(self):
        return self.__encrypted

    # String conversation method to format Asset.
    def __str__(self):
        if self.__description is not None:
            return f"{self.__name}: {self.__description} [Encrypted]"
        else:
            return f"{self.__name}: {self.__description}"
