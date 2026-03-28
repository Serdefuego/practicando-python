agendaPersonal=[]
class Agenda:
    def __init__(self):
        self.nombres="nombre"
        self.telefonos="telefono"
        self.mail="mail"
        self.menu()
    
    def menu(self):
        opccion=int(input("1 cargar contacto,2 editar contacto ,3 consultar ,4 salir"))
        match opccion:
            case 1:
                cargar()
            case 2:
                editar()
            case 3:
                consultar()
            case 4:
                salir()
    
    def cargar(self):
        seguir="si"
        while seguir=="si":
            nombre=input("ingrese nombre")
            self.nombres.append(nombre)
            telefono
            