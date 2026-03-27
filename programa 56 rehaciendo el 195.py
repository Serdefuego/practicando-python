class Alumno:
    def __init__(self):
        self.nombre=[]
        self.edad=[]
        self.menu()
      
       
    

    def menu(self):
        print("1 carga -2 muestra -3 edita -4 muestra mayores de 18")
        opccion=int(input ("ingrese opccion"))
        match opccion:
                case 1:
                   self.cargar()
                case 2:
                    self.mostrar()
                case 3:
                    self.editar()  
                case 4:
                    self.mayores()       

    def mostrar(self):
         for i in range(3):
                print ("nombre ",self.nombre[i]," edad ",self.edad[i])
         self.menu() 
    
    def editar(self):
          nombreEditar=input("ingrese nombre a editar")
          for i in range(3):
                if self.nombre[i]==nombreEditar:
                     self.nombre [i]=input("ingrese nombre editado")
                     self.edad[i]=int(input("ingrese edad editada"))
                else:
                     print("no se ha encontrado ninguna similitud")
         
          self.menu()
    
    def cargar(self):
         
         for i in range (3):
                nombres=input("ingrese nombre")
                self.nombre.append(nombres)
                edades=int(input("ingrese edad"))
                self.edad.append(edades)
         self.menu() 

    def mayores(self):
         mayores=True
         for i in range(3):
                    if self.edad[i]>18:
                        print(self.edad[i]," ",self.nombre[i])
                    else:
                        mayores=False
                        print("no hay adultos en la lista")
                        self.menu() 
         self.menu() 


persona=Alumno()


        
