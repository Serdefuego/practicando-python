class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

nuevo=Punto(3,6)
print(nuevo)