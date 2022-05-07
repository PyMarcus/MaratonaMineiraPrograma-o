"""
John wants to set up a panel containing different numbers of LEDs. He does not have many leds, he is not sure if he will be able to mount the desired number. Considering the configuration of the LEDs of the numbers below, make an algorithm that helps John to discover the number of LEDs needed to set the value.
Input
The input contains an integer N, (1 ≤ N ≤ 2000) corresponding to the number of test cases, followed by N lines, each line containing a number (1 ≤ V ≤ 10100) corresponding to the value that John wants to set with the leds.
Output
For each test case, print one line containing the number of LEDs that John needs to set the desired value, followed by the word "leds".
"""
import string


def howMuchLedsYouNeedFor(number: int) -> str:
    dict_numbers: dict[str, int] = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}
    numeber: str = str(number)
    amount: int = 0
    for digits in numeber:
        if digits in dict_numbers.keys():
            amount += dict_numbers[digits]
    print(amount)
    print(string.ascii_letters)


if __name__ == '__main__':
    value: int = 0
    try:
        limit: int = int(input())
        for _ in range(limit):
            try:
                value = int(input())
                howMuchLedsYouNeedFor(value)
            except ValueError:
                ...
    except ValueError:
        ...