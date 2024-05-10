from cesar_cypher.cesar import cesar
from recog_col_ger.reconocimiento_imagenes import color_recognise

def launcher():
    path1 = 'img/hola.jpeg'
    path2 = 'img/patata.jpeg'

    palabra1 = color_recognise(path1, 4)
    palabra2 = color_recognise(path2, 6)

    hola = ''.join(palabra1)
    patata = ''.join(palabra2)

    print(hola, patata)

    #Cifrado Cesar de 11 posiciones
    
    hola_cipher = cesar(hola, 11)
    patata_cipher = cesar(patata, 11)

    print(hola_cipher, patata_cipher)
