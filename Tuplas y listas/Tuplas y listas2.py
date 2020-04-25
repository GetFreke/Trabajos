print("Hace que no se repitan las letras por ejemplo puse Ha ha hola y no se repitio el A")

lista = []
cadena = input("Dame una cadena pe:")
for c in cadena:
    if (c not in lista):
                   lista.append(c)
print(lista)                   