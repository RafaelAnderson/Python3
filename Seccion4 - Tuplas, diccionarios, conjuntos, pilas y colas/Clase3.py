# Diccionario

diccionario = {"Persona" : "Anderson", "Ingenieria" : "Software"}

print(type(diccionario))

print(diccionario["Persona"])

diccionario["Persona"] = "Anderson"
print(diccionario)

del(diccionario["Persona"])
print(diccionario)

edades_de_alumnos = {"alumno" : 20, "otros" : 30}
print(edades_de_alumnos)

edades_de_alumnos["alumno"] +=1
print(edades_de_alumnos)

print(edades_de_alumnos["alumno"] + edades_de_alumnos["otros"])

for edades in edades_de_alumnos:
    print(edades)

for edades in edades_de_alumnos:
    print(edades,edades_de_alumnos[edades])

lista = []
lista.append(edades_de_alumnos)

print(lista)

# Lista con 2 diccionarios
edades_de_alumnos = {"mas_alumnos" : 40, "mas_genios" : 50}
lista.append(edades_de_alumnos)
print(lista)