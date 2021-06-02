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

if __name__ == '__main__':
    run()