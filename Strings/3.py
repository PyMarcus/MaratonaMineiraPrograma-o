"""
Implement a program Combiner that takes two Strings as parameters and combines them, alternating letters, starting with the first letter of the first String, followed by the first letter of the second String, then second letter of first String, etc. The remaining letters of the longer String are then appended to the end of the combination String and this combination String is returned.

Input
The input contains several test cases. The first line of input contain an integer N that indicates the number of test cases. Each test case is composed of a line containing two strings and each string contains between 1 and 50 characters, inclusive.

Output
Combine the two input strings, as shown in the example below and print the resulting string.
"""


def combination(string1: str, string2: str) -> None:
    word: str = ""
    for index, letter in enumerate(string1):
        word = word + letter + string2[index]
        if index == len(string1) - 1: word += string2[index + 1:]
    print(word)


if __name__ == '__main__':
    try:
        amount = int(input())
    except ValueError as e:
        ...
    else:
        word: str
        for n in range(amount):
            word = input()
            combination(word.split(' ')[0], word.split(' ')[1])  # test 1

