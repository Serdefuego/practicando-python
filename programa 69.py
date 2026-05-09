class Jugador:
    def __init__(self,nombre,puntaje):
        self.nombre=nombre
        self.puntaje=puntaje
        self.imprimir()
    
    def imprimir(self):
        print("el puntaje es ",self.puntaje)
    
    def __str__(self):
       
        return "el puntaje con el metodo srt "+srt(self.puntaje)

nuevo=Jugador("marcos",2000)

print(nuevo)