#Reutilizacion
#palabra reservada es def

def estudiantes():
    print("Alumnos de la UPC")

estudiantes()


def tabla_del_9():
    print("Tabla del 9:")
    for i in range(13):
        if i != 0:
            print("12 x {} = {}".format(i, i * 12))

tabla_del_9()

#variable global
def advertencia():
    global variable
    variable = "anderson el estudiante"
    print(variable)

advertencia()

variable = "Anderson"
#advertencia()
print(variable)