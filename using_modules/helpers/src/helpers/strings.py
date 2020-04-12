def extract_upper(phrase):
    """
    extract_upper takes a string and converts a list containing
    only uppercase characters from the string

    >>> extract_upper("Hi there, BoB")
    ['H', 'B', 'B']
    """

    return list(filter(str.isupper,phrase))

def extract_lower(phrase):
    return list(filter(str.islower,phrase))
