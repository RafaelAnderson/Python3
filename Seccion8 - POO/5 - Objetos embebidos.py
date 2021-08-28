class Fabrica:
    # Método Constructor
    def __init__(self, tiempo, nombre, ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print("Se creo el auto {}".format(self.nombre))
    # Método Destructor
    def __str__(self):
        return "El auto {} se fabrico en {} meses".format(self.nombre,self.tiempo)

class Listado:
    autos = []

    def __init__(self, autos = []):
        self.autos = autos

    # x -> objeto del auto
    def fabricar(self, x):
        self.autos.append(x)

    def visualizar(self):
        for x in self.autos:
            print(x)

a = Fabrica(10, "Chevrolet", 4)
l = Listado([a])

print(l.visualizar())

l.fabricar(Fabrica(15, "Porsche", 4))

print(l.visualizar())