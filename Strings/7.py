import string


def letterRange(word: str) -> str:
    alphabet: str = string.ascii_lowercase
    max: int = 0
    min: int = 0
    for index, letter in enumerate(word):
        if index == 0:
            max = alphabet.index(letter)
            min = alphabet.index(letter)
        else:
            if alphabet.index(letter) >= max:
                max = alphabet.index(letter)
            elif alphabet.index(letter) < min:
                min = alphabet.index(letter)
    print(f"{alphabet[min]}:{alphabet[max]}")


if __name__ == '__main__':
    letterRange("xyzzy".lower())