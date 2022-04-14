import math
import os
import random
import re
import sys

def breakingRecords(scores):
    high = scores[0]
    countHigh = 0
    low = scores[0]
    countLow = 0

    for i in range(len(scores)):
        if (scores[i] < low):
            low = scores[i]
            countLow += 1
        elif (scores[i] > high):
            high = scores[i]
            countHigh += 1

    return countHigh, countLow

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
