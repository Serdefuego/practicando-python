import random

numero = random.randint(0,100)

entrada = int(input("Ingrese un numero: "))
intento=0
def preguntar(numerito, entrada,intento):

    while numerito != entrada:

        if numerito > entrada:
            entrada = int(input("Ingrese un numero mas alto: "))
            intento=intento+1
        else:
            entrada = int(input("Ingrese un numero mas bajo: "))
            intento=intento+1

    print("Usted gana en ",intento," intentos")

preguntar(numero, entrada,intento)