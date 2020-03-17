
nota = int(input('Ingrese la nota del alumno: '))

def evaluacion(nota):
    valoracion = 'aprobado'
    if nota < 5:
        valoracion = "desaprobado"
    else:
        valoracion = "aprobado"

    print(valoracion)

evaluacion(nota)

    