#!/usr/bin/env python3
"""Define una clase Rectangle con área y representación."""

BaseRectangle = __import__('1-rectangle').Rectangle


class Rectangle(BaseRectangle):
    """Representa un rectángulo."""

    def area(self):
        """Calcula el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve una descripción del rectángulo."""
        return "[Rectangle] {}/{}".format(
            self.__width, self.__height
        )
