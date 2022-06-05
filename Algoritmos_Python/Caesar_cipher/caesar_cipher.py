from sys import argv, exit
from time import sleep

def caesar_cipher(string_words, position, type='encrypt'):
    labc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encrypted = []
    words = string_words.split()

    for i in words:
        if i.isalpha():
            x = [labc.index(x) for x in i]
            w = []
            for a in x:
                if type == 'encrypt':
                    h = 0
                    while True:
                        if a > 25:
                            a = 0
                        if h == position:
                            w.append(labc[a])
                            break
                        a = a + 1
                        h += 1
                elif type == 'decrypt':
                    h = 0
                    while True:
                        if a < 0:
                            a = 25
                        if h == position:
                            w.append(labc[a])
                            break
                        a = a - 1
                        h += 1
            encrypted.append("".join(w))
        else:
            print('\aEnter only words of letters!.\n')
            exit(1)
    return " ".join(encrypted)


if __name__ == '__main__':
    if len(argv) == 4:
        print(caesar_cipher(argv[1], int(argv[2]), argv[3]))
        exit(0)
    else:
        print(f'Use:\n\t\a$ python {argv[0]} "string_words" integer [encrypt|decrypt]\n')
        print('By default, encrypt the string.')
        print('You can enter strings with spaces between dobles quotes.\n')
        exit(1)
