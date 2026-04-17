class Cliente:

    suspendidos=[]                                 #variable de clase


    def __init__(self,codigo,nombre):              #inicializador
        self.codigo=codigo
        self.nombre=nombre

    def imprimir(self):                           #funcion que iprimie los datos
        print("codigo",self.codigo)
        print("nombre",self.nombre)
        self.esta_suspendido()                     #llamada a la funcion que verifica suspencion
    
    def esta_suspendido(self):                      #funcion que verifica suspencion
        if self.codigo in Cliente.suspendidos:      #si el codigo se encuentra en la variable esta suspendido
            print("esta suspendido")
        else:
            print("no esta suspendido")
            print("______________________")

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)   #esta funcion agrega el codigo del cliente al arreglo suspendidos


#bloque principal
cliente1=Cliente(1,"CARLOS")
cliente2=Cliente(2,"ANA")
cliente3=Cliente(3,"PEDRO")
cliente4=Cliente(4,"LUIS")

cliente2.suspender()
cliente3.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()