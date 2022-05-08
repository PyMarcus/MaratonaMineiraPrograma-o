"""
A letter range is a set of alphabetically consecutive letters taken from the lowercase alphabetic characters 'a' through 'z'. The lowest and highest letters of the range, separated by a colon (the character ':'), are used to represent a letter range. For example, the range "a:c" represents the consecutive letters 'a', 'b', and 'c'. (quotes are not part of the range). The range "w:z" represents the letters 'w', 'x', 'y', and 'z'. The range "m:m" respresents the single letter 'm'.

Input
Each line of input is one test case. Every test case contains one string, that can be empty and which letters may not be in alphabetical order, of lowercase letters (a-z) and spaces.

The string will contain between 0 and 50 characters, inclusive.

Output
For each test case in the input, your program must print the letter ranges ordered alphabetically by the low value of each range. Letter ranges contained in the result must represent the largest possible sequences of increasing consecutive letters found in the input text. Ignore space characters and duplicate letters contained in the input.


If the string is empty just print a new line.


For example, the string "fb xee ac" has three letter ranges, "a:c" (the letters a, b, and c), "e:f" (the letters e and f) and "x:x" (the letter x). Please refer to the examples.
"""

import string


def letterRange(words: list[str]) -> None:
    alphabet: str = string.ascii_lowercase
    max: int = 0
    min: int = 0
    for word in words:
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
    for n in range(int(input())):
        letterRange(input().lower().split(" "))