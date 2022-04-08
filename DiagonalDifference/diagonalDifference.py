import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    return abs(sum(arr[x][x] for x in range(n)) - sum(arr[x][n - x - 1] for x in range(n)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
