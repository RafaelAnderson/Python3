class Primera:
    def __init__(self):
        print("Primera clase")

    def primera(self):
        print("Método heredado de la primera clase")

class Segunda:
    def __init__(self):
        print("Segunda clase")
    def segunda(self):
        print("Método heredado de la segunda clase")

class Tercera(Primera, Segunda):
    #pass
    def tercera(self):
        print("Método heredado de la tercera clase")

#El primer valor solo se ejecuta, prioridad a las clases a la izq
#Es necesario una funcion en Primera.
herencia_multiple = Tercera()

herencia_multiple.primera()
herencia_multiple.segunda()
herencia_multiple.tercera()