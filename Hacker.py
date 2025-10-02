"""
File: Hacker.py
Description: This module represents the hacker class and has methods
that allow the hacker to...
Author: Kim Xuyen Huynh
ID: 110442620
Username: HUYKX001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Hacker:
    def __init__(self, name):
        # Constructor for the class Hacker to initialise the variables.
        self.__name = name
        self.__inventor = []
        self.__rig = None
        self.__trace_level = 0

    # String conversation method to format Hacker.
    def __str__(self):
        pass