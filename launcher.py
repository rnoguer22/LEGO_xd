from cesar_cypher.cesar import cesar
from recog_col_ger.reconocimiento_imagenes import color_recognise

def launcher():
    path = 'img/hola.jpeg'
    palabra = color_recognise(path, 4)

    print(palabra, end='')

    print('\n')

    resultado = ''

    for item in palabra:
        resultado += cesar(item) + ''
    
    return resultado

