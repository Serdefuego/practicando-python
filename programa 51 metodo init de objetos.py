class Persona:
    def __init__(self):
        self.nombre=input("ingrese nombre:")
        self.edad=int(input("ingrese edad:"))
    
    def imprimir(self):
        print("hola mi nombre es ",self.nombre," y mi edad es ",self.edad)

nuevaPersona=Persona()
nuevaPersona.imprimir()