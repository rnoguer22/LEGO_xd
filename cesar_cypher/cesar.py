def cesar(word, cipher=11):
    alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'ñ': 15, 'o': 16, 'p': 17, 'q': 18, 'r': 19, 's': 20, 't': 21, 'u': 22, 'v': 23, 'w': 24, 'x': 25, 'y': 26, 'z': 27}

    result = ''

    word = word.lower()

    for char in word:
        if char in alphabet:
            cipher_char = alphabet[char] + cipher
            if cipher_char > 27:
                cipher_char -= 27
            for key, value in alphabet.items():
                if value == cipher_char:
                    result += key
        else:
            result += char
    
    return result