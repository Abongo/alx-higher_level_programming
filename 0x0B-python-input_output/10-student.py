#!/usr/bin/python3
'''
file: 11-student.py
Classes:
-> Student
'''


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result

if __name__ == "__main__":
    Student = __import__('10-student').Student

    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)