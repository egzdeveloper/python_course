from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPelicula as cp

opcion = None

while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Película')
        print('2. Listar Películas')
        print('3. Eliminar el catálogo de películas')
        print('4. Salir')
        opcion = int(input('Elige una opción (1-4): '))

        if opcion == 1:
            nombre = input('Proporciona el nombre de la película: ')
            pelicula = Pelicula(nombre)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
        elif opcion == 4:
            exit(1)
        else:
            print('Error: Proporciona un valor correcto (1-4)')
    except Exception as e:
        print(f'Ocurrió un error: {e}')
        opcion = None
else:
    print('Saliendo del programa...')


