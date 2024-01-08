#!/usr/bin/python3
'''
function that returns True if the object is exactly
an instance of the specified class; otherwise False
'''


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of, or if obj is an instance
    of a class that inherited from, the specified class; otherwise, False."""
    return isinstance(obj, a_class)
