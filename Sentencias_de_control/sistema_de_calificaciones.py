nota = float(input('Introduce tu nota (valores entre 0 y 10): '))
calificacion = None

if nota >= 9 and nota <= 10:
    calificacion = 'A'
elif nota >= 8 and nota < 9:
    calificacion = 'B'
elif nota >= 7 and nota < 8:
    calificacion = 'C'
elif nota >= 6 and nota < 7:
    calificacion = 'D'
elif nota >= 5 and nota < 6:
    calificacion = 'E'
elif nota >= 0 and nota < 5:
    calificacion = 'F'
else:
    calificacion = 'Valor incorrecto'

print(f'Tu nota es de {nota}, con lo que tu calificación es {calificacion}')