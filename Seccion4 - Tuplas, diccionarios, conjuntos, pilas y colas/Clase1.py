# Tuplas - son listas inmutables, no se editan

t = ("Anderson", "Software", 21, [21,1,97], -97, "Hola")

print(t)
print(t[3])
print(t[2])
print(t[4])

# t[0] = "Anderson" ----> esto no es aceptable

print(t)
print(t.count("21"))