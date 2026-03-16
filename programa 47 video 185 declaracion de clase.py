class Persona:
    def inicializar(self,nom):
        self.nombre=nom
    
    def imprimir(self):
        print("hola mi nombre es",self.nombre)
    

Persona=Persona()
Persona.inicializar("marcos")
Persona.imprimir()