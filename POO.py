class Coche():
    
    def __init__(self):
        self.largoChasis = 250
        self.anchiChasis = 120
        self.__ruedas = 4
        self.enmarcha = False

    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos

        if (self.enmarcha):
            chequeo = self.chequeo_interno()

        if (self.enmarcha and chequeo):
            return "El coche esta en marcha"
        elif (self.enmarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo"
        else:
            return "El coche esta parado"

    def estado(self):
        print( "El coche tiene", coche1.__ruedas, "ruedas . Un largo de " , self.largoChasis , " y un ancho de " , self.anchiChasis )


    def chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False




coche1 = Coche()
coche2 = Coche()


print(coche1.arrancar(True))
print(coche1.estado())

print("-------------- A continuacion creamos el segundo objeto ---------------------")

print(coche2.arrancar(False))
print(coche2.estado())






