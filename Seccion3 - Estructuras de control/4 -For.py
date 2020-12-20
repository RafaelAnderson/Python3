
# FOR

lista = [1,2,3,4,5,6,7,8,9,10]
indice = 0

while indice < len(lista):
    print(lista[indice])
    indice += 1

for recorrer in lista:
    print(recorrer)

for recorrer in lista:
    recorrer *= 15
    print(recorrer)

indice = 0
for recorrer in lista:
    lista[indice] *= 10
    indice += 1
print(lista)


indice = 0
recorrer = 0
for indice, recorrer in enumerate(lista):
    lista[indice] *= 10
    print(lista)


nombre = "Rafael"
for i in nombre:
    print(i)

print(list(range(10)))


