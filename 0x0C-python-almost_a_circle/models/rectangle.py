#!/usr/bin/python3
"""Define the rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Representing the new rectangle

    Attributes:
    private class attributes:
    __width: the width of the rectangle.
    __height: the height of the rectangle.
    __x: the point x-axis.
    __y: the point y-axis.
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieve it"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set it"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieve it"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set it"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise  ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieve it"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """set it"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieve it"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """set it"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value
        of the Rectangle instance."""
        return (self.__width * self.__height)

    def display(self):
        """prints in stdout the Rectangle instance
        with the character #"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        [print("") for i in range(self.__y)]
        for j in range(self.__height):
            [print(" ", end="") for k in range(self.__x)]
            [print("#", end="") for h in range(self.__width)]
            print("")

    def __str__(self):
        """returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, 
                self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and len(args) != 0:
            i = 0
            for j in args:
                if i == 0:
                    if j is None:
                        self.__init__(self.__width, self.__height, 
                                self.__x, self.__y)
                    else:
                        self.id = j
                elif i == 1:
                    self.__width = j
                elif i == 2:
                    self.__height = j
                elif i == 3:
                    self.__x = j
                elif i == 4:
                    self.__y = j
                i += 1
        elif kwargs and len(kwargs) != 0:
            for k, h in kwargs.items():
                if k == "id":
                    if h is None:
                        self.__init__(self.__width, self.__height, 
                                self.__x, self.__y)
                    else:
                        self.id = h
                elif k == "width":
                    self.__width = h
                elif k == "height":
                    self.__height = h
                elif k == "x":
                    self.__x = h
                elif k == "y":
                    self.__y = h
