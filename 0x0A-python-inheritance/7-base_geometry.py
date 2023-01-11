#!/usr/bin/python3
"""
class module
"""


class BaseGeometry:
    """Geometry class"""

    def area(self):
        """raise exception is area is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """check if value is an integer"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
