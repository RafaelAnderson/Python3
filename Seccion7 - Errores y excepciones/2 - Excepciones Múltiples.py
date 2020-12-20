
# Manejo de errores, devolución de mensajes

variable1 = float(input('Introduce un numero: '))
# Si se escribe una letra, error!
a = 2
print('resultado = ', a*variable1)

####
try:
    variable2 = float(input('Introduce un numero: '))
    a = 2
    print('resultado = ', a*variable2)
except:
    print('Se te pidio numero :/')

####
while(True):
    try:
        variable3 = float(input('Introduce un numero: '))
        a = 2
        print('resultado = ', a * variable3)
        break # Termina la ejecucion
    except:
        print('Se te pidio un numero, intentalo de nuevo')

####
while(True):
    try:
        variable4 = float(input('Introduce un numero: '))
        a = 2
        print('resultado = ', a * variable4)
    except:
        print('Se te pidio un numero, intentalo de nuevo')
    else:
        print('Ingreso satisfactorio')
        break  # Termina la ejecucion1
    finally:
        print('Termino la ejecucion')