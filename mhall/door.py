# This class represents a simple door object
# Author: Name Cairns


## IMPORTS ##


## CONSTANTS ##


## CLASS ##

class Door:


    def __init__(self, winning_door):
        self.winning_door = winning_door


    def open_door(self):
        """Reveals what was behind the door"""
        return self.winning_door
