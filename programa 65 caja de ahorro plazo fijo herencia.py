
#creo una clase cuenta donde se crea un inicializador que captura el nombre y el monto y ademas
#hace la llamada a la funcion imprimir
#luego a la funcion imprimir no la definimos dentro de esta clase , ya que se ira modificando en las otras clases hijas
class Cuenta():
    def __init__(self):
        self.nombre=input("ingrese nombre")
        self.monto=int(input("ingrese monto"))
        self.imprimir()
    
    def imprimir(self):
        pass

#creo una clase caja de ahorro hija de la clase cuenta , tambien posee un inicializador automatico
#pero este inicializador inicia con las capturas de la clase padre , osea el nombre y el monto
#la diferencia es que en esta clase si definimos la accion de la funcion imprimir
class CajaDeAhorro(Cuenta):
    def __init__(self):
        super().__init__()
    
    def imprimir(self):
        print("usted cuenta con: ",self.monto)
    
#creo otra clase llamada plazofijo hija de la clase cuenta ,por lo que iniciara pidiendo el nombre y el monto
#ya que es la accion del inicializador automatico init de la clase padre
#en esta clase ,vamos a pedir que se carge el valor de la variable tiempo
#y tambien en esta clase vamos a estar modificando la funcion imprimir por lo tanto volveos a defininarla dentro
class PlazoFijo(Cuenta):
    def __init__(self):
        super().__init__()
        self.tiempo=int(input("ingrese cantidad de dias"))

    def imprimir(self):
        print("su plazo fijo rindio :",((self.monto*0.27)+self.monto))

nuevoPLazo=PlazoFijo()
nuevoPLazo.imprimir()