from PIL import Image
import numpy as np
import pandas as pd

# Asignar colores conocidos
colores_conocidos = {
    'Negro': [0, 0, 0], 'Gris oscuro': [115, 116, 115], 'Gris claro': [160, 160, 160], 'Beige': [155, 144, 114], 'Beige oscuro': [143, 131, 97], 'Vasija': [148, 128, 108], 'Teja': [150, 75, 45], 'Marron': [37, 73, 141], 'Granate': [128, 0, 32], 'Rojo': [255, 0, 0], 'Naranja': [255, 165, 0], 'Pure de calabaza': [237, 145, 33], 'Amarillo': [255, 255, 0], 'Pistacho': [147, 197, 114], 'Verde': [0, 255, 0], 'Verde vidrio': [144, 238, 144], 'Verde bosque': [34, 139, 34], 'Azul marino': [0, 0, 128], 'Azul electrico': [0, 0, 255], 'Azul cielo': [135, 206, 250], 'Azul turquesa': [64, 224, 208], 'Violeta': [143, 0, 255], 'Morado': [128, 0, 128], 'Rosa fucsia': [255, 0, 255], 'Rosa': [255, 192, 203], 'Rosa chicle': [255, 183, 197], 'Blanco': [255, 255, 255]
    
}

# Función para calcular la distancia entre colores
def distancia_color(color1, color2):
    return np.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(color1, color2)))

# Función para encontrar el color más cercano
def encontrar_color_mas_cercano(color):
    distancias = {nombre: distancia_color(color, rgb) for nombre, rgb in colores_conocidos.items()}
    return min(distancias, key=distancias.get)

# Función para calcular la distancia euclidiana entre dos colores
def distancia_color(color1, color2):
    return np.linalg.norm(color1 - color2)

# Función para encontrar el color LEGO más cercano al color de la ficha
def encontrar_color_mas_cercano(color, colores_conocidos):
    distancias = {nombre: distancia_color(color, rgb) for nombre, rgb in colores_conocidos.items()}
    return min(distancias, key=distancias.get)

# Cargar la imagen
def color_recognise(path, n):
    image = Image.open(path)
    image = image.convert('RGB')
    pixels = np.array(image)
    df = pd.read_csv('recog_col_ger/colores.csv')

    # Suponiendo que las fichas están alineadas horizontalmente en el centro de la imagen
    height = pixels.shape[0]
    width = pixels.shape[1]
    middle_y = height // 2

    # Suponer que tenemos un número conocido de fichas de LEGO alineadas
    ancho_ficha = width // n

    # Almacenar los colores encontrados para cada ficha
    colores_encontrados = []

    # Iterar sobre cada ficha LEGO en la imagen
    for i in range(n):
        # Calcular el inicio y el fin de la región de la ficha en x
        start_x = i * ancho_ficha
        end_x = (i + 1) * ancho_ficha

        # Extraer la región de la ficha
        ficha_region = pixels[middle_y, start_x:end_x]

        # Calcular el color promedio de la ficha
        color_promedio = np.mean(ficha_region, axis=0).astype(int)
        
        # Encontrar el color LEGO más cercano al color promedio encontrado
        color_lego_mas_cercano = encontrar_color_mas_cercano(color_promedio, colores_conocidos)
        
        # Añadir el color identificado a la lista de colores encontrados
        colores_encontrados.append(color_lego_mas_cercano)

    palabra = []

    for item in colores_encontrados:
        if df['Color'].str.contains(item).any():
            palabra.append(df.loc[df["Color"] == item, "Letra"].values[0])
        else:
            print(f'Color: {item} - Nombre: No encontrado')
    
    return palabra




