class Familia:
    hijos = ["marcos", "carolina"]

    def __init__(self):
        self.padre = "ricardo"
        self.madre = "azucena"

    def __str__(self):
        return "padre: " + self.padre + " madre: " + self.madre + " hijos: " + str(self.hijos)

grupo = Familia()
print(grupo)