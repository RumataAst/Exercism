""" Function used to respond
    Based on input there are several response options.
"""

def response(hey_bob):
    """ Choosing response

        :param hey_bob: str - initial string.
        :return: str - reply to the initial string.

        Function takes initial sentence and then based on criteria such as all caps, question and if the string is empy
        send reply.
    """
    initial_string = hey_bob.strip()
    if len(initial_string) == 0:
        return "Fine. Be that way!"

    all_capital = initial_string.isupper()
    question = initial_string[-1] == "?"
    if question and all_capital:
        return "Calm down, I know what I'm doing!"
    if question:
        return "Sure."
    if all_capital:
        return "Whoa, chill out!"
    return "Whatever."