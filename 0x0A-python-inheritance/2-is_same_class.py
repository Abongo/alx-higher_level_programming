#!/usr/bin/python3
"""Module containing is_same_class method"""


def is_same_class(obj, a_class):
    """Returns True if obj is an instance of a_class; otherwise, False."""
    return type(obj) == a_class
