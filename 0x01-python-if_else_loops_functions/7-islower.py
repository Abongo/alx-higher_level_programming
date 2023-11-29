#!/usr/bin/python3
def islower(c):
    if 65 <= ord(c) <= 90:
        return False
    elif 97 <= ord(c) <= 122:
        return True
    else:
        return False
