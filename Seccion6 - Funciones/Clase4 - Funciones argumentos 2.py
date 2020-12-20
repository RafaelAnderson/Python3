
def alumnos(valor):
    valor *= 3

variable = 15
alumnos(variable)
print(variable)

def listas(numero):
    for x,i in enumerate(numero):
        numero[x] *= 3

lista = [50,100,150]
listas(lista)
print(lista)

##
def alumno(valor):
    return valor * 3

var = 15
var = alumno(var)
print(var)

##### Fibonacci

def fibonacci(numero):
    n1, n2 = 0, 1
    count = 0

    if numero <= 0:
        print("Ingrese un numero entero")
    elif numero == 1:
        print("Secuencias de fibonacci ", numero, ":")
        print(n1)
    else:
        print("Números:")
        while count < numero:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

fibonacci(5)










