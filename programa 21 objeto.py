Persona={
    "nombre":"marcos",
    "edad":36,
    "idioma":"español"
}
def presentarse(objeto):
    print("hola mi nombre es ",objeto["nombre"])
    print("tengo ",objeto["edad"])
    print("y hablo en  ",objeto["idioma"])
    print("mi hobbie es ",objeto["hobbie"])


Persona["hobbie"]="programacion"

presentarse(Persona)
