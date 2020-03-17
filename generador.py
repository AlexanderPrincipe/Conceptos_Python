def generaPares(limite):
    numero = 1

    while numero < limite:
        yield numero * 2
        numero = numero + 1

devuelvePares = generaPares(10)

for i in devuelvePares:
    print(i)



   


   

