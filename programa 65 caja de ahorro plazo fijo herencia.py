class Cuenta():
    def __init__(self):
        self.nombre=input("ingrese nombre")
        self.monto=int(input("ingrese monto"))
        self.imprimir()
    
    def imprimir(self):
        pass


class CajaDeAhorro(Cuenta):
    def __init__(self):
        super().__init__()
    
    def imprimir(self):
        print("usted cuenta con: ",self.monto)
    

class PlazoFijo(Cuenta):
    def __init__(self):
        super().__init__()
        self.tiempo=int(input("ingrese cantidad de dias"))

    def imprimir(self):
        print("su plazo fijo rindio :",((self.monto*0.27)+self.monto))

nuevoPLazo=PlazoFijo()
nuevoPLazo.imprimir()