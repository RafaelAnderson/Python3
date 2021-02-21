# Computadora: clase; Procesador, Grafica: atributos

###     1° forma
class Computadora:
    pass
#
pc = Computadora()
#
pc.codigo = "HDBI-1974689"
pc.fabricante = "Intol"

print("El codigo de mi computadora es {} y es del fabricante {}".format(pc.codigo, pc.fabricante))


###     2° forma -> aunque no es muy utilizado
class Celular:
    Intol = False
#
phone = Celular()
#
print(phone.Intol)

###     3° forma
class Televisor:
    Azul = False
    # "init " sirve para la creacion del objeto
    def __init__(self):
        print("Se ha creado un televisor")

    def Pintar(self):
        self.Azul = True
        print("Pintando el tv de azul")

    def confirmacion(self):
        if(self.Azul):
            print("El televisor ya esta pintado")
        else:
            print("El televisor aun no esta pintado")

tv = Televisor() # ---> lo que debe mostrar es la creacion del televisor
print(Televisor.Azul) # -> al ejecutar esta linea, nos lanzara False
print(tv.Azul) # -> nos muestra True, debido a que el self cambia el estado original de Plasma

print("Confirmacion: ")
tv = Televisor()
tv.confirmacion()
tv.Pintar()
tv.confirmacion()