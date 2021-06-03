# 

import random
n_words = 171
random_words = []
random_lines = [random.randint(1, n_words) for i in range(1, 4)]



def run():
    with open('./words.txt', 'r', encoding='utf8') as f:
        line = 0
        for word in f:
            line += 1
            if line == random_lines[0] or line == random_lines[1] or line == random_lines[2]:
                random_words.append(word.strip())
    print(random_words[0])
    game(random_words[0])

def game(word):
    attemps = 5
    hidden_word = []
    isHere = False
    hangmang = list(enumerate(word))
    for i in range(0, len(word)):
        hidden_word.append(' _')

    for i in range(len(word)):
        print(' _', end='')
    
    while attemps > 0:
        letter = input('\nEscribe una letra: ')
        #afirmacion: letter no puede ser un numero
        for i in range(0, len(word)):
            if letter == hangmang[i][1]:
                hidden_word[i] = hangmang[i][1].upper()
                isHere = True
        print(''.join(hidden_word))
        if isHere != True:
            attemps = attemps - 1
        else:
            isHere = False
           

if __name__ == '__main__':
    run()