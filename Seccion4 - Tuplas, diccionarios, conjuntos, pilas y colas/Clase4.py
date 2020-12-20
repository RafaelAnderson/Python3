#Pilas
#Solo agregar y sacar

apilar = [1,2,3,4]
apilar.append(3)
apilar.append(36)
apilar.append(8)
apilar.append(9)
print(apilar)

# Desapilar el ultimo elemento, se pierde
apilar.pop()
print(apilar)

# Desapilar sin perder el elemento.
no_perderlo = apilar.pop()
print(no_perderlo)
no_perderlo = apilar.pop()
print(no_perderlo)
no_perderlo = apilar.pop()
print(no_perderlo)