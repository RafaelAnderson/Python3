
#Conjuntos

#conjunto = set() <---- Crear conjunto vacio
con = {5,4,3}

print(con)

con.add(2)
print(con)

con.add(6)
print(con)

con.add('H')
print(con)

con.add('B')
print(con)

con.add('y')
print(con)

con.add('Z')
print(con)


coleccion = {"Anderson", "programadores", "ingenieria"}
print("Rafael" in coleccion)

elementos = {"gato", "gato", "gato", "gato", "gato"}
print(elementos)


lista = [5,5,6,6,7,7]
print(lista)

# Lista a conjunto
conjuntito = set(lista)
print(conjuntito)

# Filtrar los caracteres
cadena = "Yo quiero mucho a mis gatos <3"
print(set(cadena))