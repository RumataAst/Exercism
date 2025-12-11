def is_isogram(string):
    """ Function takes string and determine if this word/phrase is isogram or not

        :param string: str Word or a phrase
        :return: bool Isogram = True
    """
    string = string.lower()
    skip = ["-", " "]
    for letter in string:
        if string.count(letter) != 1 and letter not in skip:
            return False
    return True