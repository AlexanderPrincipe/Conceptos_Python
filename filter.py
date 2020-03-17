def pares(num):
    if num%2 == 0:
        return True

numeros = [17,34,56,86,34,23,67,78]


print(list(filter(pares, numeros)))