import re

lista_nombres = ['Ana Gomez',
                 'Maria Martin',
                 'Sandra Lopez',
                 'Santiago Martin',
                 'Sandra Fernendez',
                 'Iñaki Peña',
                 'niños',
                 'niñas']

for elemento in lista_nombres:
    if re.findall('^Sandra', elemento):
        print(elemento)

print("******************")

for elemento in lista_nombres:
    if re.findall('Martin$', elemento):
        print(elemento)

print("******************")

for elemento in lista_nombres:
    if re.findall('[ñ]', elemento):
        print(elemento)

print("******************")

for elemento in lista_nombres:
    if re.findall('niñ[oa]s', elemento):
        print(elemento)
    
    


