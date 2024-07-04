cadena = 'Hola Mundo'
print (f'Texto a iterar: {cadena}')
texto = ''

for letra in cadena:
    texto += letra + ' '

print(f'Texto resultante: {texto}')

print('\nUso de break en la letra \'a\': ')
texto = ''
for letra in cadena:
    texto += letra + ' '
    if letra == 'a':
        print('Letra \'a\' encontrada')
        break

print(f'Texto resultante: {texto}')

print('\nUso de continue para encontrar número pares: ')
texto = ''

for i in range(10):
    if i % 2 != 0:
        continue
    texto += str(i) + ' '

print(f'Los número pares del 0 al 10 son: {texto}')
