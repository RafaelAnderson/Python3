
#funcion recursiva, aquella que se llama a si misma

def cuenta_atras(segundos):
    segundos -= 1
    if segundos > 0:
        print(segundos)
        cuenta_atras(segundos)
    else:
        print('Se acabo el tiempo')

cuenta_atras(10)

## Funcion integrada - transforma una cadena a un entero
e = int('14')
print(e)

## Entero a binario
print(bin(14))

## Numero a hexagesimal
print(hex(14))

# Valor absoluto de un numero
print(abs(-14))

# Redondear
print(round(14.5)) #redondeo hacia arriba
print(round(15.4)) #redondeo hacia abajo

# Ayuda de Python
help()