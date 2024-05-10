from PIL import Image
import numpy as np
import pandas as pd

# Asignar colores conocidos
colores_conocidos = {'Negro': [5, 19, 29], 'Gris oscuro': [108, 110, 104], 'Gris claro': [171, 173, 172], 'Beige': [220, 188, 129], 'Beige oscuro': [180, 132, 85], 'Vasija': [169, 85, 0], 'Teja': [173, 97, 64], 'Marron': [148, 81, 72], 'Granate': [135, 43, 23], 'Rojo': [201, 26, 29], 'Naranja': [255, 128, 20], 'Pure de calabaza': [250, 156, 28], 'Amarillo': [248, 241, 132], 'Pistacho': [199, 210, 60], 'Verde': [0, 100, 0], 'Verde vidrio': [0, 146, 71], 'Verde bosque': [0, 74, 45], 'Azul marino': [27, 42, 52], 'Azul electrico': [0, 87, 153], 'Azul cielo': [0, 153, 212], 'Azul turquesa': [63, 182, 158], 'Violeta': [255, 213, 237], 'Morado': [129, 0, 123], 'Rosa fucsia': [199, 0, 57], 'Rosa': [255, 105, 143], 'Rosa chicle': [252, 151, 172], 'Blanco': [255, 255, 255]}

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




