from cesar_cypher.cesar import cesar
from recog_col_ger.reconocimiento_imagenes import color_recognise

def launcher():
    path = 'img/patata.jpeg'
    palabra = color_recognise(path, 6)

    resultado = ''

    for item in palabra:
        resultado += cesar(item) + ''
    
    return resultado

print(launcher())