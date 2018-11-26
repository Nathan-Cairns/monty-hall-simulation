#!/usr/bin/env python3

# This class represents a game instance
# Author: Nathan Cairns


## IMPORTS ##


import random


## CLASS ##


class Game:


    def __init__(self, num_doors):
        """INIT"""
        self.num_doors = num_doors
        self.door_one = None
        self.door_two = None
        self.doors = []
        self._generate_doors()


    def _generate_doors(self):
        """Generates the array of doors for the game"""
        for _ in range(self.num_doors):
            self.doors.append(False)

        # Randomly select the door with the car
        self.car_door = random.randint(0, self.num_doors - 1) 
        self.doors[self.car_door] = True
        print(self.doors)


    def _open_all_other_doors(self):
        """Opens all other doors"""
        if self.door_one == self.car_door:
            second_door_range = list(range(0, self.door_one))
            second_door_range.extend(range(self.door_one, self.num_doors - 1))
            self.door_two = random.choice(second_door_range)
        else:
            self.door_two = self.car_door


    def _check_door(self, door_num):
        """Checks to see if door num contains the car
        Parameters:
            door_num: the index of the door to check
        Returns:
        """
        if door_num == self.car_door:
            return True
        return False


    def second_door_index(self):
        """Shows the other door narrowed down by monty
        Returns:
            The index of the door selected by monty
        """
        if self.door_one is None:
            raise RuntimeError("Error: The select_first_door() function must"
                    + " be called first")
        return self.door_two


    def select_first_door(self, door_num):
        """selects a door
        Parameters:
            door_num -- the index of the door to select
        """
        print(self.car_door + 1)
        if door_num > self.num_doors or door_num < 0:
            raise ValueError("Error: Input must be between 0 and {}".format(num_doors))

        self.door_one = door_num
        self._open_all_other_doors()


    def select_final_door(self, door_num):
        """Selects the final door to open
        Parameters:
            door_num -- the door to open. Either 1 or 2
        Returns: 
            true if user selects right, false otherwise
        """
        print(self.car_door + 1)
        if door_num == 1:
            return self._check_door(self.door_one)
        elif door_num == 2:
            return self._check_door(self.door_two)
        else:
            raise ValueError("Error: Input must be either 1 or 2")

