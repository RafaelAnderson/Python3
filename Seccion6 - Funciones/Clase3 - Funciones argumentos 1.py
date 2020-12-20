# return devuelve true o false

def multiplicar(a = None, b = None):
    if a == None or b ==None:
        print("Variables no ingresadas")
        return
    return print("{} x {} = {}".format(a,b,a*b))

multiplicar(2,4)