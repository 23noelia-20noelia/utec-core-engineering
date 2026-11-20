#!/usr/bin/env python3
"""Define una clase Square con representación personalizada."""

SquareBase = __import__('1-square').Square


class Square(SquareBase):
    """Representa un cuadrado."""

    def __str__(self):
        """Devuelve una descripción del cuadrado."""
        return "[Square] {}/{}".format(
            self.__size, self.__size
        )
