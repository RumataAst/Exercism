""" Function used to calculate if the year is a leap year or not
    based on the conditions.
"""

def leap_year(year):
    """Check whether a given year is a leap year.

        :param year: int - year value.
        :return: bool - True if leap year, otherwise False.
    
        Leap year conditions:
            - Year must be divisible by 4.
            - If divisible by 100, it is not a leap year unless divisible by 400.
    """
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False