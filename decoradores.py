def funcion_decoradora(funcion_parametro):
    def funcion_interna():

        print("Vamos a realizar un calculo: ")
        funcion_parametro()
        print("Hemos terminado el calculo")

    return funcion_interna

# La funcion decoradora recibe como parametro a la funcion suma, que en la funcion_decoradora toma el nombre de funcion_parametro

@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)


suma()

resta()