# https://www.hackerrank.com/challenges/electronics-shop/problem

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#

def getMoneySpent(keyboards, drives, b, l = -1):
    for x in keyboards:
        for y in drives:
            if(l<=x+y<=b): l=x+y
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()