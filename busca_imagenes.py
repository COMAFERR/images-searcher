import os
import shutil

def copiar_imagenes(csv_file, carpeta_imagenes, carpeta_destino):
    imagenes_encontradas: int = 0
    imagenes_falladas: int = 0
    
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Leer el archivo CSV
    with open(csv_file, 'r', newline='') as file:
        cabecera = file.readline().strip()
        next(cabecera)  # Saltar la primera fila si contiene encabezados

        for row in file:
            id_producto = row[0]  # Suponiendo que el ID del producto está en la primera columna
            nombre_imagen = f"{id_producto}.jpg"  # Nombre de archivo de la imagen
            
            # Comprobar si la imagen existe en la carpeta de imágenes
            ruta_imagen_origen = os.path.join(carpeta_imagenes, nombre_imagen)
            if os.path.exists(ruta_imagen_origen):
                # Copiar la imagen a la carpeta de destino
                ruta_imagen_destino = os.path.join(carpeta_destino, nombre_imagen)
                shutil.copyfile(ruta_imagen_origen, ruta_imagen_destino)
                imagenes_encontradas = imagenes_encontradas + 1
                print(f"Imagen para el producto {id_producto} copiada correctamente.")
            else:
                imagenes_falladas = imagenes_falladas + 1
                print(f"No se encontró imagen para el producto {id_producto}.")

    print(f"Se han encontrado {imagenes_encontradas} imágenes, y han fallado {imagenes_falladas} imágenes.")        

# Rutas de los archivos y carpetas
csv_file = "articulos.csv"
carpeta_imagenes = "."
carpeta_destino = "EXPORTAR"

# Llamar a la función para copiar imágenes
copiar_imagenes(csv_file, carpeta_imagenes, carpeta_destino)
