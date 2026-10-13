#!/usr/bin/env python3
numero = __import__('random').randint(-10000, 10000) 
ultimo_digito = abs(numero) % 10 

if numero < 0:
    ultimo_digito = -ultimo_digito

if ultimo_digito > 5:
    print("El último dígito de {} es {} y es más grande que 5".format(numero, ultimo_digito))

elif ultimo_digito == 0:
    print("El último dígito de {} es {} y es 0".format(numero, ultimo_digito))


else:
    print("El último digito de {} es {} es menor que 6 y no es 0".format(numero, ultimo_digito))

