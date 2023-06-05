#!/usr/bin/python3
"""Define the rectangle class"""


class Rectangle:
    """Representing the rectangle
    Attributes:
    number_of_instances (int): the number of rectangle instances.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize new rectangle.
        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        Raises:
        TypeError: width and height must be integers.
        ValueError: width and height must be >= 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """retrieve it"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set it"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return("")
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print the message Bye rectangle... (... being 3 dots not ellipsis)
        when an instance of Rectangle is deleted"""
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
