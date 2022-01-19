def is_pangram(sentence):
    letras = "abcdefghijklmnopqrstuvwxyz"
    letts = []
    for word in sentence.lower().split():
        for lett in letras:
            if lett in word:
                if lett not in letts:
                    letts.append(lett)
    letts.sort()
    if "".join(letts) == letras:
        return True
    return False


is_pangram("The quick brown fox jumps over the lazy dog.")


