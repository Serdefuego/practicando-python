class Persona():
    def __init__(self):
        self.nombre=input("ingrese nombre")
        self.edad=int(input("ingrese edad"))
        self.imprimir()
    def imprimir(self):
        print("mi nombre es: ",self.nombre)
        print("mi edad es de: ",self.edad)

class Hijo(Persona):                  #aqui estoy aportandole la herencia de a clase persona
    def __init__(self):               #comienzo nomalmente
       super().__init__()             #aqui es donde inicio el init de la clase persona con la palabra super()
       self.premio=input("ingrese premio")
       self.prueba()

    def prueba(self):
        if self.edad>18:
            print("ganaste tu: ",self.premio)
        else:
            print("sos menor a 19 no obtenes premios")


objeto=Hijo()
