#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if char.islower():
            result += char.upper()
        else:
            result += char
    print("{1}".format(str, result))
