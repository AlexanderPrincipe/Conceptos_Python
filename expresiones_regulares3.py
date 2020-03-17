import re

lista_nombres = ['Ma1',
                 'Se1',
                 'Ba1',
                 'Ba2',
                 'Se2',
                 'BaA',
                 'BaB',
                 'BaC',
                 'Ba3',
                 'Ba4']

for elemento in lista_nombres:
    if re.findall('Ba[0-3A-B]', elemento):
        print(elemento)


