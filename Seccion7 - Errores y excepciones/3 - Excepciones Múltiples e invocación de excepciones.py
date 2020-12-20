
try:
    a = float(input('Numero: '))
    10/a
except Exception as x:
    print(type(x).__name__) #__name__ nombre del error

####
try:
    b = float(input('Numero: '))
    10/b
except TypeError:
    print('Esto es una cadena')
except ValueError:
    print('Debe ser un numero')
except ZeroDivisionError:
    print('No ser puede dividir por cero')
except Exception as y:
    print(type(y).__name__)

####
def estudiante(curso = None):
    try:
        if curso is None:
            raise ValueError
    except ValueError:
        print('Insertar curso!!')

estudiante('Arquitectura de Computadoras')
estudiante()