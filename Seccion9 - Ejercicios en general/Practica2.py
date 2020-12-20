## Tabla de multiplicar dinamica
def tabla_dinamica1():
    a = int(input("Ingresa el numero del que deseas conocer la tabla de multiplicar: "))
    print("Tabla del {}:".format(a))
    for i in range(13):
        if i != 0:
            print("{} x {} = {}".format(a, i, i * a))

def tabla_dinamica2(a):
    print("Tabla del {}:".format(a))
    for i in range(13):
        if i != 0:
            print("{} x {} = {}".format(a, i, i * a))

tabla_dinamica1()
tabla_dinamica2(11)