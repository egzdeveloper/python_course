import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='*******',
    host='localhost',
    port='5432',
    database='test_db'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            # Recuperar todos los registros
            cursor.execute('SELECT * FROM persona')
            registros = cursor.fetchall()
            print(registros)

            # Recuperar sólo un registro
            cursor.execute('SELECT * FROM persona WHERE id_persona = 1')
            registro = cursor.fetchall()
            print(registro)

            # Insertar un registro
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Carlos', 'González', 'cgoz@gmail.com')
            cursor.execute(sentencia, valores)
            num_registros = cursor.rowcount
            print(f'Registros insertados: {num_registros}')

            # Insertar varios registros al mismo tiempo
            valores = (('Ramón', 'Perez', 'rperez@gmail.com'), ('Anto', 'Luis', 'antoluis@gmail.com'))
            cursor.executemany(sentencia, valores)
            num_registros = cursor.rowcount
            print(f'Registros insertados: {num_registros}')

            # Eliminar un registro
            sentencia = 'DELETE FROM persona WHERE id_persona = 4'
            cursor.execute(sentencia)
            num_registros = cursor.rowcount
            print(f'Registros eliminados: {num_registros}')
except Exception as e:
    print(f'Error: {e}')
finally:
    conexion.close()