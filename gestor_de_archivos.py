# librerías ---------------------------------------------------------------------------------------------------
import os

# Funciones de gestión de archivos ----------------------------------------------------------------------------

def crear_directorio(nombre):
    ruta_final = nombre
    contador = 1 # para verificar si el nombre ya existe y crear uno nuevo con un número al final

    #Busca un nombre libre: "carpeta (1)", "carpeta (2)", etc, para que no haya error por repetir nombres.
    while os.path.exists(ruta_final):
        ruta_final = f"{nombre} ({contador})"
        contador += 1

    # Crea el directorio con el nombre libre encontrado
    os.makedirs(ruta_final)

    # Mensaje final
    return "se ha creado el directorio: " + ruta_final



def crear_archivo_txt(nombre):
    # Nos aseguramos de que el archivo tenga la extensión ".txt" al final
    if not nombre.endswith(".txt"):
        # Sino la tiene la pegamos al final
        nombre += ".txt"

    # Separamos el nombre del archivo por si debemos modificar el nombre para que no se repita
    base, extension = os.path.splitext(nombre)
    ruta_final = nombre
    contador = 1

    # Busca un nombre libre: "nombre (1).txt", "nombre (2).txt", etc.
    while os.path.exists(ruta_final):
        ruta_final = f"{base} ({contador}){extension}"
        contador += 1

    # descriptor de archivo: es un número entero que representa un archivo abierto en el sistema operativo.
    descriptor = os.open(ruta_final, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    # os.O_CREAT Activa la creación. Le ordena al sistema operativo que, si el archivo indicado en ruta_final no existe en el disco, lo cree desde cero.
    # os.O_EXCL garantiza que no se sobrescriba si algo se creó en ese mismo instante
    # os.O_WRONLY indica que el archivo se abrirá en modo de escritura, es obligatorio incluir este modo para poder crear un archivo nuevo.
    
    os.close(descriptor) # Cerramos el descriptor de archivo para liberar recursos

    return "se ha creado el archivo: " + ruta_final




# Programa principal ---------------------------------------------------------------------------------

if __name__ == "__main__":
    while True:
        print("\nBienvenido al Gestor de Archivos")
        print("Seleccione una opción válida:\n")
        print("1. Crear un directorio")
        print("2. Crear un archivo de texto")
        print("3. Escribir información en un archivo")
        print("4. Leer el contenido de un archivo")
        print("5. Renombrar un archivo")
        print("6. Copiar un archivo")
        print("7. Eliminar un archivo")
        print("8. Listar archivos de un directorio")
        print("9. Consultar información de un archivo")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")

        # Menú de opciones --------------------------------------------------------------

        if opcion == "1":
            input_nombre = input("\nIngrese el nombre del directorio a crear: ")
            print(crear_directorio(input_nombre))
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            input_nombre = input("\nIngrese el nombre del archivo a crear: ")
            print(crear_archivo_txt(input_nombre))
            input("\nPresione Enter para continuar...")

        elif opcion == "0": # Salida
            break

        else: # Opción no válida
            print("\nOpción no válida. Por favor, seleccione una opción del 0 al 9\n")
            input("\nPresione Enter para continuar...")