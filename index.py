def suma(numero1, numero2):
    return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    return numero1 * numero2

def division(numero1, numero2):
    return numero1 / numero2

numero1 = int(input('Ingrese un numero: '))
numero2 = int(input('Ingrese otro numero: '))




print('la suma de  {}  y  {}  es  {}'.format(numero1, numero2, suma(numero1, numero2)))
print('la resta de  {}  y  {}  es  {}'.format(numero1, numero2, resta(numero1, numero2)))
print('la multiplicacion de  {}  y  {}  es  {}'.format(numero1, numero2, multiplicacion(numero1, numero2)))
print('la division de  {}  y  {}  es  {}'.format(numero1, numero2, division(numero1, numero2)))