#!/usr/bin/env python3
"""Define una clase Square que puede imprimir un cuadrado."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa el cuadrado."""
        self.size = size

    @property
    def size(self):
        """Devuelve el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Valida y actualiza el tamaño del cuadrado."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size * self.__size

    def my_print(self):
        """Imprime el cuadrado utilizando el carácter #."""
        for i in range(self.__size):
            print("#" * self.__size)
