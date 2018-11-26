#!/usr/bin/env python3


# IMPORTS #


from .context import game


# CONSTANTS #


YES = {'yes','y', ''}
NO = {'no','n'}


# FUNCTIONS #


def multiple_simulations(num_sims):
    """Runs multiple simulations and prints statistics
    Parameters:
        num_sims -- Run without changing door num_sims times and run with
            changing door num_sims times.
    """
    assert True #TODO


def main():
    print("Monty Hall Simulator")

    # Create a game with as many doors as required.
    num_doors = int(input("How many doors would you like to test with?: "))
    mhallgame = game.Game(num_doors)

    first_door_idx = int(input("Select the number of the door you wish to"
            + " open (1 to {}): ".format(num_doors)))

    # Select the door and monty narrows down
    first_door_idx = first_door_idx - 1
    mhallgame.select_first_door(first_door_idx)
    second_door = mhallgame.second_door_index()

    # Check if user wants to change door
    print("You selected door {}".format(first_door_idx + 1))
    print("Monty reveals all other doors except for door {} contain goats".format(second_door + 1))
    change_door = input("Do you wish to change from the door you have selected? (y/n): ")

    correct = False
    if change_door in YES:
        correct = mhallgame.select_final_door(2)
    elif change_door in NO:
        correct = mhallgame.select_final_door(1)
    else:
        print("Error: Incorrect value inputted. Value must be y or n")

    if correct:
        print("Congrats you won a car!")
    else:
        print("Sorry you are going home with a goat")


# MAIN #


if __name__ == "__main__":
    main()
