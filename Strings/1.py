"""
You have been asked to build a simple encryption program. This program should be able to send coded messages without someone been able to read them. The process is very simple. It is divided into two parts.

First, each uppercase or lowercase letter must be shifted three positions to the right, according to the ASCII table: letter 'a' should become letter 'd', letter 'y' must become the character '|' and so on. Second, each line must be reversed. After being reversed, all characters from the half on (truncated) must be moved one position to the left in ASCII. In this case, 'b' becomes 'a' and 'a' becomes '`'.

For example, if the resulting word of the first part is "tesla", the letters "sla" should be moved one position to the left. However, if the resulting word of the first part is "t#$A", the letters "$A" are to be displaced.

Input
The input contains a number of cases of test. The first line of each case of test contains an integer N (1 ≤ N ≤ 1 * 10⁴), indicating the number of lines the problem should encrypt. The following N lines contain M characters each M (1 ≤ M ≤ 1 * 10³).
Output
For each input, you must present the encrypted message.
"""
import string


def encrypt(word: str) -> str:
    # ascii_characteres: list[chr] = [chr(integer) for integer in range(127)]
    ascii_characteres:list[chr] = [ch for ch in string.ascii_letters]
    encrypted: str = ""
    letter_indice: dict[str, int] = {}
    for ind, ch in enumerate(ascii_characteres): # armazena posicoes da tabela ascii conforme letras
        for index, char in enumerate(word):
            if char == ch:
                letter_indice[char] = ind + 3
    for key, value in letter_indice.items():
        word = word.replace(key, ascii_characteres[value])  # troca para 3 posicoes acima
    word = word[::-1]
    half: int = len(word) // 2
    new_word: str = word[half:]
    for index, value in enumerate(word):
        if value in ascii_characteres:
            new_word = new_word.replace(value, ascii_characteres[ascii_characteres.index(value) - 1])
    encrypted = word[:half] + new_word
    return encrypted


if __name__ == '__main__':
    response: str = encrypt("Texto #3")
    print(response)
