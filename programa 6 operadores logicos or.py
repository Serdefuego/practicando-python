num = int(input("Ingrese numero: "))
condicion="si"
while condicion=="si":
    if num == 7 or num == 3:
        print("Ganó");
        print("desea intentarlo nuevamente?");
        condicion=input("si/no")
        num = int(input("Ingrese numero: ")) 
    else:
        print("perdió") 
        print("desea intentarlo nuevamente?");
        condicion=input("si/no")
      
        if condicion!="si":
            print("gracias por juegar hasta luego")
        else:
              num = int(input("Ingrese numero: ")) 

