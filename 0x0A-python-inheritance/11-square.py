#!/usr/bin/python3
"""Also inherits from Rectangle(9-rectangle.py)
task based on 10-square.py"""
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
