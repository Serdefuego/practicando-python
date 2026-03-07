meses=("enero","febrero","marzo","abril","mayo","junio",
       "julio","agosto","septiembre","octubre","noviembre","diciembre")

def devuelveRestantes(mes):
    buscar=int(input("ingrese numero "))
    print ("el numero de mes es:",buscar,"y se trata de ",mes[buscar-1],",los meses restantes son:")
    buscado=mes[buscar:]
    for items in buscado:
        print(items)

devuelveRestantes(meses)

