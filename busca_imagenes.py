import os
import shutil   # Copia archivos y carpetas.

def copiar_imagenes(csv, carpeta_imagenes, carpeta_destino):
    cont_imgs_encontradas: int = 0
    cont_imgs_falladas: int = 0
    
    # Creamos la carpeta de destino si no existe.
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Leer el archivo CSV
    with open(csv, mode='r', encoding='utf-8') as file:
        cabecera = file.readline().strip()
        # next(cabecera)  # Saltar la primera fila si contiene encabezados

        for linea in file:
            id_producto = (linea.split(";")[0])[1:]  # Suponiendo que el ID del producto está en la primera columna
            nombre_imagen = f"{id_producto}.jpg"  # Nombre de archivo de la imagen
            
            # Comprobar si la imagen existe en la carpeta de imágenes
            ruta_imagen_origen = os.path.join(carpeta_imagenes, nombre_imagen)
            # print (f"imagen: {nombre_imagen} - ruta {ruta_imagen_origen}")

            if os.path.exists(ruta_imagen_origen):
                # Copiar la imagen a la carpeta de destino
                ruta_imagen_destino = os.path.join(carpeta_destino, nombre_imagen)
                shutil.copyfile(ruta_imagen_origen, ruta_imagen_destino)

                # Contamos la imagen como encontrada.
                cont_imgs_encontradas = cont_imgs_encontradas + 1
                print(f"Imagen para el producto {id_producto} copiada correctamente.")
            else:
                # Imagen no encontrada.
                cont_imgs_falladas = cont_imgs_falladas + 1
                print(f"No se encontró imagen para el producto {id_producto}.")

    print(f"Se han encontrado {cont_imgs_encontradas} imágenes, y han fallado {cont_imgs_falladas} imágenes.")        

# Llamar a la función para copiar imágenes
copiar_imagenes(csv= "articulos.csv", carpeta_imagenes= ".", carpeta_destino= "EXPORTAR")
