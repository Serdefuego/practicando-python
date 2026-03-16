class cuadrante:
    def __init__(self):
        self.x=int(input("ingrese cuandrante x"))
        self.y=int(input("ingrese cuadrante y"))
    
    def calcularPosicion(self):
        if self.x>0 and self.y>0:
            print("se encuentra en el cuadrante 1")
        elif self.x >0 and self.y<0:
            print("se encuantra en el cuadrante 2")
        elif self.x<0 and self.y<0:
            print("se encuentra en el cuadrante 3")
        elif self.x<0 and self.y>0:
            print("se encuentra en el cuadrante 4")

posicion=cuadrante()
posicion.calcularPosicion()
        