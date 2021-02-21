
class Televisor:
    Azul = False
    # "init " sirve para la creacion del objeto
    def __init__(self, aplicaciones = None, color = None):
        self.aplicaciones = aplicaciones #referencia a toda la clase
        self.color = color

        if aplicaciones is not None and color is not None:
            print("Se ha fabricado un televisor, tiene {} aplicaciones instaladas y es de color {}".format(aplicaciones, color))

    def Pintar(self):
        self.Azul = True

    def confirmacion(self):
        if(self.Azul):
            print("El televisor ya esta pintado")
        else:
            print("El televisor aun no esta pintado")

#
tv = Televisor()
tv = Televisor("2")
tv = Televisor("3", "azul") # Este seria el unico en imprimir, puesto que los demas no tienen los parametros completos