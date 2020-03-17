def suma (num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print('No se puede dividir entre 0')
        return "Operacion erronea"

while True:
    try:
        num1 = int(input('Ingrese un numero: '))
        num2 = int(input('Ingrese otro numero: '))
        break
    
    except ValueError:
        print('Valores introducidos no correctos, solo se permite numeros')
    
print(suma(num1,num2))