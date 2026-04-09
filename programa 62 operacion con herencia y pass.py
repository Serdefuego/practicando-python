class Operacion():
    def __init__(self):
        self.valor1=0
        self.valor2=0
        self.resultado=0
    
    def cargar1(self):
        self.valor1=int(input("ingrese primer valor"))
    def cargar2(self):
        self.valor2=int(input("ingrese segundo valor"))

    def mostrar_resultado(self):
        print(self.resultado)

    def operar(self):
        pass            #aqui lo dejamos en blanco con pass 
                        #porque lo vamos a modificar en las clases hijas


class Suma(Operacion):
    def operar(self): #aqui es donde sobre escribe a la funcion declarada en la clase padre
        self.resultado=self.valor1+self.valor2

class Resta(Operacion):
    def operar(self):
        self.resultado=self.valor1-self.valor2

#bloque principal
suma1=Suma()
suma1.cargar1()
suma1.cargar2 () 
suma1.operar() 
suma1.mostrar_resultado()