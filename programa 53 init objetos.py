class Cuadrado:
    def __init__(self):
        self.lado = int(input("Ingrese lado del cuadrado: "))

    def superficie(self):
        resultado = self.lado ** 2
        print("La superficie es:", resultado)


primero = Cuadrado()
primero.superficie()