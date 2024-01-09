#!/usr/bin/python3
'''
file: 11-student.py
Classes:
-> Student
'''


class Student:

    def __init__(self, first_name, last_name, age):
        '''
        Constructor
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        Retrieves a dictionary representation
        of a Student instance
        '''
        return vars(self)
