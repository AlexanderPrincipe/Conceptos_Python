listanumeros = []
listapares = []
listamultiplos = [[],[],[],[],[]]

for i in range(1, 11):  
    listanumeros.append(i)


cantidadlista = len(listapares)

for j in listanumeros:
    if j % 2 == 0:
        listapares.append(j)
        for k in listapares:
            for l in range(2,5):
                for m in range(1,cantidadlista):
                    listamultiplos[m].append(k*l)
               
                

print(listamultiplos)








