#!/usr/bin/python3
"""
rectangle module
"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("Width Must be int")
            if value <= 0:
                raise ValueError("Width Must be grater than 0")
            self.width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("Height Must be int")
            if value <= 0:
                raise ValueError("height Must be grater than 0")

        @property
        def x(self):
            pass

        @x.setter
        def x(self, value):
            pass

        @property
        def y(self):
            pass

        @y.setter
        def y(self, value):
            pass
