# Mejorar la interfaz
# Añadir la racha
# Manejar errores

import random
import os

n_words = 171
random_words = []
random_lines = [random.randint(1, n_words) for i in range(1, 4)]
levels = 3


def run():
    """Escoje las palabras para el juego y gestiona los niveles
    No tiene parametros
    Return mensaje de victoria
    """
    with open('./words.txt', 'r', encoding='utf8') as f:
        line = 0
        for word in f:
            line += 1
            if line == random_lines[0] or line == random_lines[1] or line == random_lines[2]:
                random_words.append(word.strip())
    for i in range(0, levels):
        level = i + 1
        os.system('cls')
        game(random_words[i], level)
        print('Felicidades haz ganado!')


def game(word, level):
    """Contiene la logica del juego (revisar que la letra este en la palabra, llevar la cuenta de los intentos etc...)
    word string palabra que debes adivinar
    level int nivel actual
    return en caso de acertar con la palabra es NULL o si no das con la palabra muestra mensaje de derrota
    """
    attemps = 5
    founds = 0
    hidden_word = []
    isHere = False
    hangmang = list(enumerate(word))

    for i in range(0, len(word)):
        hidden_word.append(' _')

    print(f'\nLEVEL: {level}\n')
    for i in range(len(word)):
        print(' _', end='')

    while attemps > 0:
        if founds == len(word):
            return
        else:
            letter = input('\n\nEscribe una letra: ')
            print(type(letter))
            for i in range(0, len(word)):
                if letter == hangmang[i][1]:
                    hidden_word[i] = hangmang[i][1].upper()
                    founds += 1
                    isHere = True
            os.system('cls')
            print(f'\nLEVEL: {level}\n')
            print(''.join(hidden_word))
            if isHere != True:
                attemps = attemps - 1
            else:
                isHere = False

    if attemps == 0:
        os.system('cls')
        with open('./lose.txt', 'r', encoding='utf8') as f:
            for line in f:
                print(line)
        print(f'Lo siento haz perdido la palabra era {word}')
        exit()


if __name__ == '__main__':
    run()