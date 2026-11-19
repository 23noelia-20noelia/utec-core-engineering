#!/usr/bin/env python3
"""Define una clase Square con un método para calcular el área."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa el cuadrado y valida su tamaño."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size * self.__size
