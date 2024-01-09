#!/usr/bin/python3
""" save items to a file."""

import json


def save_to_json_file(my_obj, filename):
    '''
    Writes object to text file using JSON
    '''
    if filename is None:
        return
    with open(filename, 'w', encoding='utf-8') as f:
        json_var = json.dump(my_obj, f)
