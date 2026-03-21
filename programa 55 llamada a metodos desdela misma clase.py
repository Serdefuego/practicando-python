class Operaciones:
    def __init__(self):
        self.numeroUno=int(input("ingrese primer numero"))
        self.numeroDos=int(input("ingrese segundo numero"))
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()
    
    def multiplicacion(self):
        multiplicado=self.numeroUno*self.numeroDos
        print("la multiplicacion es ",multiplicado)
    
    def suma(self):
        sumado=self.numeroUno+self.numeroDos
        print("la suma es de ",sumado)
    
    def resta(self):
        restado=self.numeroUno-self.numeroDos
        print("la resta es ",restado)
    
    def division(self):
        dividido=self.numeroUno//self.numeroDos
        if dividido:
            print("el resusltado de la division es ",dividido)
        else:
            print("hay un error en la division, el primer numero debe ser mayor")

operacion=Operaciones()
