#!/usr/bin/python3
"""
rectangle module
"""
from models.base import Base


class Rectangle(Base):

    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializez a rectangle"""

        """Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
