
#tupla
def argumento(*tu):
    for tus in tu:
        print(tus)

argumento('Rafael Ponte', 'Ingenieria', 'Software')

###################
def nombre_diccionario(**lo):
    #print(lo)
    for x in lo:
        print(x, ": ", lo[x])

nombre_diccionario(rafael='Anderson', ingenieria='Software', notas=[13,14,15])

###################

def bandera(*tu, **lo):
    b = 0
    for tus in tu:
        b += tus
    print(b)
    for x in lo:
        print(x, ": ", lo[x])

bandera(1, 2, 3, 4, rafael='Anderson', ingenieria='Software', notas=[13,14,15])