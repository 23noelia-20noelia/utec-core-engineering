#!/usr/bin/env python3
"""Define la clase BaseGeometry."""


class BaseGeometry:
    """Representa una geometría básica."""

    def area(self):
        """Indica que el cálculo del área no está implementado."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que value sea un entero mayor que cero."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
