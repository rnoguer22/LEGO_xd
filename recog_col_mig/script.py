import cv2
import numpy as np
from sklearn.cluster import KMeans
import webcolors

def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]


def extract_dominant_colors(image_path, num_colors=5):
    # Leer imagen
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Redimensionar para disminuir el tiempo de procesamiento
    image = cv2.resize(image, (64, 64), interpolation=cv2.INTER_AREA)
    
    # Cambiar forma de la imagen a una lista de pixeles
    pixels = image.reshape((-1, 3))
    
    # Usar KMeans para encontrar colores dominantes
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    
    # Obtener los colores dominantes
    dominant_colors = kmeans.cluster_centers_
    
    return dominant_colors.astype(int)

# Ejemplo de uso:
dominant_colors = extract_dominant_colors("negro.jpg")
dominant_colors = dominant_colors[1]
color_name = closest_color(dominant_colors)
print(f"El nombre del color más cercano al RGB {dominant_colors} es {color_name}.")
"""
for i in range(len(dominant_colors)):
    color_name = closest_color(dominant_colors[i])
    print(f"El nombre del color más cercano al RGB {dominant_colors[i]} es {color_name}.")
"""