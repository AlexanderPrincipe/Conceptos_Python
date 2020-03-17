diccionario = {"Alemania": "Berlin", "Francia": "Paris", "España":"Madrid"}
diccionario["Italia"]="Roma"

print(diccionario["Francia"])
print(diccionario)

del diccionario["España"]
print(diccionario.keys())
print(diccionario.values())
print(len(diccionario))