class Agenda:
    def __init__(self):
       '''--------------- creo un objeto contacto que alojara el nombre como clave,telefono y mail como valor------ '''
       self.contacto={}
       self.menu()


    ''' ------------------el menu de opcciones----------------------------------------- '''   

    def menu(self):
        opccion=int(input("1-cargar 2-mostrar 3-editar 4-salir"))
        match opccion:
            case 1:
                cargar()
            case 2:
                mostrar()
            case 3:
                editar()
            case 4:
                print("gracias por utilizar este programa ")
        

        
        def cargar(self):
            nombre=input("ingrese nombre")
            telefono=input("ingrese telefono")
            mail=input("ingrese mail")
            self.contacto[nombre]=(telefono,mail)
            print("_____________________________")
            
        def mostrar(self):
            print("toda la agenda")
            for persona in self.contacto:
                print(persona,self.contacto[persona][0],self.contacto[persona][1])
            print("_____________________________")
        
        def editar(self):
            nombre=input("ingrese el nombre de la persona que quiere modificar")
            if nombre in self.contacto:
                 nombre=input("ingrese nombre")
                 telefono=input("ingrese telefono")
                 mail=input("ingrese mail")
                 self.contacto[nombre]=(telefono,mail)
            else:
                print("no existe un contacto con dicho nombre")


            