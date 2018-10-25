# This class represents a game instance
# Author: Nathan Cairns


## IMPORTS ##


import .door


## CONSTANTS ##


## CLASS ##


class Game:


    def __init__(self, num_doors):
        self.num_doors = num_doors
        self._generate_doors()


    def _generate_doors(self):
        """Generates the array of doors for the game"""
        for num_doors:
            # Todo populate array of doors and add to self
            assert True


    def _open_all_other_doors(self, door_num):
        """Opens all other doors"""


    def open_door(self, door_num):
        """Opens a door"""
        assert True



