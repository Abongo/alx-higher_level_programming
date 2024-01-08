#!/usr/bin/python3
class MyList(list):
    """A class that inherits list and has a method for printing sorted list."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
