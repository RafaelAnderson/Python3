#If

if True:
    print("Imprime prueba")

if False:
    print("Imprime prueba")

variable = 10

if variable == 10:
    print("La variable es {}".format(variable))

if variable != 9:
    print("La variable no es 9")


if variable != 10:
    print("La variable es {}".format(variable))
    if variable != 9:
        print("La variable no es 9")