#!/usr/bin/python3
"""Define the student class"""


class Student:
    """Representing the new student.

    Attributes:
    first_name (string): the first name of the student.
    last_name (string): the last name of the student.
    age (int): the age of the student.
    Methods:
    __init__ - initializes the Student instance.
    to_json - retrieves dictionary repr of Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation
        of a Student instance"""
        return self.__dict__
