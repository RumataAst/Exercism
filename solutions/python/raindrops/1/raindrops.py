""" Simple function to train %.
"""

def convert(number):
    """
    Convert a number into a string based on specific divisibility rules.

    :param number: int - input value.
    :return: str - transformed value according to the rules below.

    Rules:
        - If divisible by 3, append "Pling".
        - If divisible by 5, append "Plang".
        - If divisible by 7, append "Plong".
        - If not divisible by any of the above, return the number as a string.
    """
    result = []

    if number % 3 == 0:
        result.append("Pling")
    if number % 5 == 0:
        result.append("Plang")
    if number % 7 == 0:
        result.append("Plong")

    return "".join(result) if result else str(number)