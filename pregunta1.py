
n = int(input('Ingrese un numero: '))

if n >=1 and n<=100:

    if (n%2 != 0):
        print('Weird')
    elif (n%2 == 0 and n<=5 and n>=2 ):
        print('Not Weird')
    elif (n%2 == 0 and n>=6 and n<=20 ):
        print('Weird')
    elif (n%2 == 0 and  n > 20 ):
        print('Not Weird')

else:
    print('error')

    