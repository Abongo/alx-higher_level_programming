#!/usr/bin/python3
def print_square(size):
    """
    Prints a square with the character #.

    Args:
    size (int): Size length of the square.

    Raises:
    TypeError: If size is not an integer or if size is a float.
    ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
