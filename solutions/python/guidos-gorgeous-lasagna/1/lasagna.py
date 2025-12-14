"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    return (EXPECTED_BAKE_TIME - elapsed_bake_time)


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers: int):
    """Calculate the bake time remaining.

    :param number_of_layers: int - number of layers of the lasagna.
    :return: int - time (in minutes) expected to make that number of layers.

    Function that takes the number of layers that will be in the lasagna
    an argument and returns how many minutes would take to make that many layers.
    """
    minutes_for_layer = 2
    return (number_of_layers * minutes_for_layer)


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate the elapsed cooking time in minutes.

    :param number_of_layers: int - number of layers of the lasagna.
    :param elapsed_bake_time: int - number of minutes the lasagna has spent baking already.
    :return: int - total elapsed cooking time (in minutes).

    Function that takes the actual minutes the lasagna has been in the 
    oven as an argument plus the preparation time and returns how many 
    minutes you have been cooking.
    """
    return (preparation_time_in_minutes(number_of_layers) + elapsed_bake_time)


# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
