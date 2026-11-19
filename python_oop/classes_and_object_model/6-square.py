#!/usr/bin/env python3
"""Define una clase Square con posición e impresión personalizada."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el cuadrado con tamaño y posición."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Devuelve el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Valida y actualiza el tamaño."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Devuelve la posición del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Valida y actualiza la posición."""
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(type(n) is int and n >= 0 for n in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size * self.__size

    def my_print(self):
        """Imprime el cuadrado respetando su posición."""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Devuelve la representación del cuadrado."""
        if self.__size == 0:
            return ""

        lines = [""] * self.__position[1]
        for i in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lines)
