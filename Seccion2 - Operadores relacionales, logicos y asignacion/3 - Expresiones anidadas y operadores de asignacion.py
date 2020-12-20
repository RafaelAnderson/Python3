
# Expresiones anidadas y operadores de asignación

primero = 8
segundo = 10

print(primero * segundo - 4**primero or not (primero % segundo) == 0)
print(primero * segundo - 4**primero <= 8 or not (primero % segundo) == 0)

valor = 10
print(valor)

valor += 10
print(valor)

valor *=2
print(valor)

valor %=3
print(valor)