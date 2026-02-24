🧩 Programa 8 – Suma de valores almacenados en una lista
📌 Descripción

Este programa permite al usuario ingresar tres números, almacenarlos en una lista y luego calcular la suma total de los valores ingresados.

Se utiliza una variable acumuladora (resultado) para ir sumando cada elemento de la lista.

🧠 Conceptos trabajados

Listas dinámicas

Conversión de tipos (int)

Método .append()

Variable acumuladora

Bucle for para recorrer valores directamente

Procesamiento de datos almacenados

💻 Código
valores = []
resultado = 0

for i in range(3):
    valor = int(input("ingrese numero: "))
    valores.append(valor)

for i in valores:
    resultado += i

print("la suma de los numeros ingresados es de:", resultado)