#https://pythondiario.com/ejercicios-de-programacion-python - Ejercicio 1

#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
def max():
    print("Programa que devuelve el número máximo")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    if num1 > num2:
        print("{} es el máximo".format(num1))
    elif num1 < num2:
        print("{} es el máximo".format(num2))
    else:
        print("Son iguales:")
max()
print()
#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos. (Considerando hallar el máximo valor posible)
def max_de_tres():
    print("Programa que devuelve el máximo valor entre 3 números")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))
    if num2 <= num1 and num3 <= num1:
        print("{} es el máximo".format(num1))
    elif num1 <= num2 and num3 <= num2:
        print("{} es el máximo".format(num2))
    elif num1 <= num3 and num2 <= num3:
        print("{} es el máximo".format(num3))
max_de_tres()
print()
#Definir una función que calcule la longitud de una lista o una cadena dada.
def longitud(cadena):
    elementos = 0
    print("Calculando la longitud de la cadena: {}".format(cadena))
    for x in cadena:
        elementos = elementos+1
    print(elementos)

longitud("Hola me llamo Rafael")
print()
#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False
def vocal():
    contador = 0
    caracter = input("Ingresa un caracter: ")
    vocales = ["a","e","i","o","u"]
    for x in vocales:
        if x == caracter:
            print("True")
            break
        else: contador = contador + 1
    if contador == 5:
        print("False")
vocal()
print()
#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
def sum():
    sumatoria = 0
    n = 1
    cadena = []
    numeros = int(input("¿Cuántos números quieres ingresar? Rpta: "))

    while n <= numeros:
        num = float(input("Ingresa numero {}: ".format(n)))
        cadena.append(num)
        n = n + 1

    for x in cadena:
        sumatoria = sumatoria + x

    print("La sumatoria es: {}".format(sumatoria))
sum()
print()
def multip():
    sumatoria = 1
    n = 1
    cadena = []
    numeros = int(input("¿Cuántos números quieres ingresar? Rpta: "))

    while n <= numeros:
        num = float(input("Ingresa numero {}: ".format(n)))
        cadena.append(num)
        n = n + 1

    for x in cadena:
        sumatoria = sumatoria * x

    print("El producto total es: {}".format(sumatoria))
multip()
print()
#Definir una función inversa() que calcule la inversión de una cadena.
def reverse():
    texto = input("Ingresar un texto: ")
    print("El texto invertido es: ",texto[::-1])
reverse()
print()
#Definir una función es_palindromo() que reconoce palíndromos. True si es cierto.
def palindromo():
    print("Programa que verifica si una palabra es palindromo")
    texto = input("Ingresa un texto: ")
    texto_invertido = texto[::-1]
    if texto == texto_invertido:
        print("True")
    else: print("False")
palindromo()
print()
#Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
def superposicion():
    aux = 0
    contador1 = 1
    contador2 = 1
    lista1 = []
    lista2 = []
    print("Para detener el ciclo escribe: stop")
    while contador1 != 0:
        num = input("Cadena 1, texto {}: ".format(contador1))
        if num != "stop":
            lista1.append(num)
            contador1 = contador1 + 1
        else: contador1 = 0

    while contador2 != 0:
        num = input("Cadena 2, texto {}: ".format(contador2))
        if num != "stop":
            lista2.append(num)
            contador2 = contador2 + 1
        else: contador2 = 0

    for x in lista1:
        for y in lista2:
            if x == y:
                print("True")
                aux = 1
                break # Termina si hay coincidencia
    if aux == 0:
        print("False")
superposicion()
print()
#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n.
#Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"
def generar_n_caracteres():
    numero = float(input("Ingresa un numero: "))
    caracter = input("Ingresa caracter: ")
    contador = 1
    cadena = []

    while contador <= numero:
        cadena.append(caracter)
        contador = contador + 1
    print("Resultado: ",''.join(cadena))
generar_n_caracteres()
print()
#Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.
#Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
#****
#*********
#*******
def histograma_procedimiento():
    lista = []
    contador = 0
    print("Escribe para detener: stop")
    while contador != 1:
        num = int(input("Ingresa numero: "))
        if num != -1:
            lista.append(num)
        else: contador = 1
    print(lista)

    for x in lista:
        auxiliar = 0
        list2 = []
        while auxiliar < x:
            list2.append("*")
            auxiliar = auxiliar + 1
        print("#",''.join(list2))
histograma_procedimiento()