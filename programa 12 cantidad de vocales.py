frase=input("ingrese frase")
preparado=frase.lower()
a=0
e=0
i=0
o=0
u=0
for x in range(len(preparado)):
    if preparado[x]=="a":
        a+=1
    elif preparado[x]=="e":
        e+=1
    elif preparado[x]=="i":
        i+=1
    elif preparado[x]=="u":
        u+=1    
    elif preparado[x]=="o":
        o+=1
print("tu frase contiene ", a ," :a ", e ," :e ",i ," :i ", o ," :o ", u ," :u "  )