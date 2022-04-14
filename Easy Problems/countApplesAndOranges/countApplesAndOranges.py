import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    countValidApples = 0
    countValidOranges = 0

    for i in range(len(apples)):
        apples[i] = (apples[i] + a)
        if (apples[i] in range(s, t + 1)):
            countValidApples += 1

    for j in range(len(oranges)):
        oranges[j] = (oranges[j] + b)
        if (oranges[j] in range(s, t + 1)):
            countValidOranges += 1

    print(countValidApples)
    print(countValidOranges)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

