#Else

variable = 9

if variable % 2 == 0:
    print("No hay residuo")
else:
    print("Si hay residuo")


frase = "hola"

if frase == "No":
    print("Bienvenido")
elif frase == "hola": ## Entra si no entra en el otro
    print("nos estan saludando")
else:
    print("Esto es algo que no da ningun resultado")


nota = float(input("coloca la nota: "))
if nota >= 13:
    print("Estas aprobado!")
elif nota >= 10 and nota < 13:
    print("Puedes mejorar")
else:
    print("Debes estudiar!!!!!!!!!")
