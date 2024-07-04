edad = int(input('Introduce tu edad: '))
etapa = None

if edad >= 0 and edad < 10:
    etapa = 'La infancia es increíble...'
elif edad >= 10 and edad < 20:
    etapa = 'Muchos cambios y mucho estudio...'
elif edad >= 20 and edad < 30:
    etapa = 'Amor y comienza el trabajo...'
else:
    etapa = 'Etapa de vida no reconocida'

print(f'Tu edad es {edad} y la etapa de tu vida es: {etapa}')