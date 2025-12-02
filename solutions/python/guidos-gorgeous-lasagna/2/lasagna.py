"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    


def preparation_time_in_minutes(number_of_layers):
    """Calculate the time spent on layers preparation for lasagna.

    :param number_of_layers: int - number of layers.
    :return: int - number of layers multiplied by  'PREPARATION_TIME'.

    Function that takes the number of layers lasagna has and then calculates time required to prepare lasagna
    by multiplying it to 'PREPARATION_TIME' needed.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the time spent in kitchen.

    :param number_of_layers: int - number of layers.
    :param elapsed_bake_time: int - baking time already elapsed.

    :return: int - number of minutes spent preparing the dish.

    Function that calculates the time spent in kitchen by 
    summarazing time preparing lasagna and then cooking it.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

