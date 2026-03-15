class Triangulo:

    def lados(self,lado_1,lado_2,lado_3):
        self.lado_uno = lado_1
        self.lado_dos = lado_2
        self.lado_tres = lado_3
    
    def imprimir(self):
        if self.lado_uno == self.lado_dos and self.lado_uno == self.lado_tres:
            print("es equilatero")
        else:
            print("no es equilatero")

    def mayor(self):
        mayor = max(self.lado_uno, self.lado_dos, self.lado_tres)
        print("el mayor de los lados es:", mayor)


triangulo = Triangulo()

triangulo.lados(3,2,5)
triangulo.imprimir()
triangulo.mayor()