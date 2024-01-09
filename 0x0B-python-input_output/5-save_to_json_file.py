#!/usr/bin/python3
'''
Write a function that returns the JSON
representation of an object (string)
'''


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using a JSON representation."""
    import json

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
