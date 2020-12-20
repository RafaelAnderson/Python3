
# Practica

print("Elige la alternativa que mas te agrade")
inicio = input("Escribre empezar para iniciar el programa: ")

while(inicio == "empezar"):
    print(""" ¿Qué deseas realizar?
            Escribe la opción:
            \t 1. Quiero que me saludes
            \t 2. Quiero multiplicar
            \t 3. Quiero que finalize el programa""")

    opcion = input()
    if opcion == "1":
        print("Hola :D")
    elif opcion == "2":
        num1 = input("Ingresa primer numero: ")
        num2 = input("Ingresa segundo numero: ")
        print("El producto es: {}".format(num1*num2))
    elif opcion == "3":
        print("Programa finalizado. Hasta luego")
        break
    else:
        print("Opcion incorrecta")

