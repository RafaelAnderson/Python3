#################### Herencia
# Super Clase
class Fabrica():
    def __init__(self, marca, nombre, precio, descripcion):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def __str__(self):
        return """\
        MARCA\t\t{}
        NOMBRE\t\t{}
        PRECIO\t\t{}
        DESCRIPCION\t{}""".format(self.marca,self.nombre,self.precio,self.descripcion)

class Auto(Fabrica):
    pass

z = Auto('Ford', 'Ranger', 100000, 'Camionera')
print(z)

class Deportivo(Fabrica):
    ruedas = ""
    distribuidor = ""

    def __str__(self):
        return """\
        MARCA\t\t{}
        NOMBRE\t\t{}
        PRECIO\t\t{}
        DESCRIPCION\t{}
        RUEDAS\t{}""".format(self.marca,self.nombre,self.precio,self.descripcion,self.ruedas)
print("")
y = Deportivo('Lamborghini', 'Murciélago', 250000, 'Carrera')
print(y)