# Dada la siguiente tupla, crear una lista que sólo incluya los números menos a 5
tupla = (13, 1, 8, 3, 2, 5, 8)

lista = []

for i in tupla:
    if i < 5:
        lista.append(i)

lista.sort()
print(lista, end=' ')