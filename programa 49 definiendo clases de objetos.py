class Persona:
    def crear (self,name,edge):
        self.nombre=name
        self.edad=edge

    def imprimir(self):
        print("mi nombre es ",self.nombre)
        print("mi edad es ",self.edad)

    def mayor(self):
        if self.edad>18:
            print("soy mayor de edad")
        else:
            print("soy menor de edad")

nueva=Persona()

nueva.crear("marcos",36)
nueva.imprimir()
nueva.mayor()

