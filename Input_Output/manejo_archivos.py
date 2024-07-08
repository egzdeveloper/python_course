try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adiós')
except Exception as e:
    print(e)
finally:
    archivo.close()

archivo = open('prueba.txt', 'r', encoding='utf8')
print(archivo.read())
archivo.close()
