import re

cadena1 = "Jara Lopez"
cadena2 = "Antonio Gomez"
cadena3 = "lara Lopez"
cadena4 = "565467547"

if re.match(".ara", cadena1, re.IGNORECASE):
    print("Se encontro el nombre")
else:
    print("No lo hemos encontrado")

if re.match("\d", cadena4):
    print("Es digito")
else:
    print("No es digito")