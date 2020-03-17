diassemana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 2]

diassemana.append(50)
diassemana.insert(2,100)
diassemana.remove(100)
diassemana.remove(2)
diassemana.remove(50)
diassemana.pop()


for dias in diassemana:
    print(dias)

print(diassemana.index("miercoles"))

print("viernes" in diassemana)


 

