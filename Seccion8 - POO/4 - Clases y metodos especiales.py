
class Fabrica:
    # Método Constructor
    def __init__(self, tiempo, nombre, ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print("Se creo el auto {}".format(self.nombre))
    # Método Destructor
    def __del__(self):
        print("Se eliminó el auto {}".format(self.nombre))

a = Fabrica(10, "Chevrolet", 4)

class Compania:
    # Método Constructor
    def __init__(self, tiempo, nombre, ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print("Se creo el auto {}".format(self.nombre))
    # Método Destructor
    def __del__(self):
        print("Se eliminó el auto {}".format(self.nombre))

    #def __str__(self):
        #return "{} se fabricó con éxito, en el tiempo {} y tiene {} ruedas".format(self.nombre,self.tiempo,self.ruedas)

    def __len__(self): #Medir la longitud
        return self.tiempo

b = Compania(11, "Lamborghini", 4)
#print(str(b))
print(len(b))