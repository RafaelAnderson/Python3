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

class Accesorios(Fabrica):
    anio_fab = 2000
    fabricante = ""

    def __str__(self):
        return """\
        MARCA\t\t{}
        NOMBRE\t\t{}
        PRECIO\t\t{}
        DESCRIPCION\t{}
        FABRICANTE\t{}""".format(self.marca,self.nombre,self.precio,self.descripcion,self.fabricante)

auto = Auto('Ford', 'Ranger', 100000, 'Camionera')
#print(z)
deportivo = Deportivo('Lamborghini', 'Murciélago', 250000, 'Carrera')
#print(y)
accesorios = Accesorios('OEN', 'Faro delantero', 200, 'Luces amarillas')
#print(x)

fabrica = [auto, deportivo]
fabrica.append(accesorios)
print(fabrica)

for arreglo in fabrica:
    print(arreglo, "\n")

for arreglo2 in fabrica:
    print(arreglo2.marca, "\t",arreglo2.precio)

## Para evitar errores de clases que no tengan un atributo
for arreglo3 in fabrica:
    if(isinstance(arreglo3, Auto)):
        print(arreglo3.marca, arreglo3.nombre)
    elif(isinstance(arreglo3, Deportivo)):
        print(arreglo3.marca, arreglo3.ruedas)
    elif(isinstance(arreglo3, Accesorios)):
        print(arreglo3.marca, arreglo3.nombre, arreglo3.anio_fab)

## Recibir datos dentro de funciones (Polimorfismo)

# copy - genera una copia de un elemento
import copy
copia_accesorios = copy.copy(accesorios)
print(copia_accesorios)

def Descuento_auto(t, descuento):
    t.precio = t.precio - (t.precio / 100 * descuento)

Descuento_auto(copia_accesorios, 10)
print(accesorios.precio)
print(copia_accesorios.precio)