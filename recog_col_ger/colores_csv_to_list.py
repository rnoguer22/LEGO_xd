import csv
import ast  # Para convertir el string de RGB a una lista de enteros

def extraer_colores_del_csv(nombre_archivo):
    colores_dict = {}
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            color_nombre = fila['Color']
            rgb_str = fila['RGB']
            # Convertir la cadena de texto RGB que se lee como "[255, 255, 255]" a una lista de enteros
            rgb_list = ast.literal_eval(rgb_str)
            colores_dict[color_nombre] = rgb_list
    return colores_dict

# Usar la función, asumiendo que el archivo se llama 'colores.csv'
colores = extraer_colores_del_csv('colores.csv')
print(colores)
