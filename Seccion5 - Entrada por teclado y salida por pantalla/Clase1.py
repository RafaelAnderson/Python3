#Entrada por teclado

ingreso = input("Ingresa tu clase: ")
print(ingreso)

listas = []
print("Ingresa ya mismo 5 numeros: ")
for i in range(5):
    listas.append(input("Ingresa numero {}: ".format(i+1)))

print(listas)