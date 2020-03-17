
def areaCuadrado(lado):

    """Calcula el area de un cuadrado elevando
     al cuadrado el lado pasado por parametro"""

    print("El area del cuadrado es: " +  str(lado*lado))

def areaTriangulo(base,altura):

    """Calcula el area de un triangulo utilizando
     los parametros base y altura"""

    print("El area del triangulo es: ", str((base*altura)/2))

print(areaCuadrado(10))
print(areaCuadrado.__doc__)

help(areaTriangulo)
