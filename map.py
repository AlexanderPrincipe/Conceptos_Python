class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [

Empleado("Juan", "Director", 75000),
Empleado("Pedro", "Presidente", 180000),
Empleado("Sara", "Secretaria", 45000),
Empleado("Marta", "Psicologa", 65000)

]

salarios_altos = filter(lambda empleado:empleado.salario > 50000, listaEmpleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)