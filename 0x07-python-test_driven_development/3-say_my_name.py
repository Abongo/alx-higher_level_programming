#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Args:
    first_name (str): First name.
    last_name (str, optional): Last name (default is "").

    Raises:
    TypeError: If first_name or last_name is not a string.
    """


    if isinstance(first_name, str) is False:
        raise TypeError('first_name must be a string')
    if isinstance(last_name, str) is False:
        raise TypeError('last_name must be a string')

    print('My name is {:s} {:s}'.format(first_name, last_name))
