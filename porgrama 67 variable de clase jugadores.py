class Jugador:
    variableDeClase=30
    def __init__(self ,nombre, puntaje):
        self.nombre=nombre
        self.puntaje=puntaje
        self.imprimir()
        self.pasarTiempo()
    
    def imprimir(self):
        print("nombre: ",self.nombre)
        print("puntaje: ",self.puntaje)
        print("tiempo",Jugador.variableDeClase)
        print("____________")

    def pasarTiempo(self):
        Jugador.variableDeClase=Jugador.variableDeClase-1            

pedro=Jugador("PEDRO",10)

pedro.imprimir()
pablo=Jugador("pablo",50)
pablo.imprimir()