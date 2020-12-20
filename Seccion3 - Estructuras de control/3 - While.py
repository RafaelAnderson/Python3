
# While permite iterar, realiza una accion varias veces

iteracion = 1

while iteracion <= 3:
    print(iteracion)
    iteracion += 1
else:
    print("Fin :)")

valor1 = 1
while valor1 <= 3:
    print(valor1)
    valor1 += 1
    break
else:
    print("Fin :)")


valorn = 0
while valorn <= 10:
    valorn += 1
    if valorn == 4:
        print("Van", valorn)
else:
    print("Se termino")