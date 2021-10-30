# https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(z, arr):
    k = arr[-1]    
    while((k<arr[z]) and (z>=0)):
        arr[z+1],z = arr[z],z-1
        print(*arr)
    arr[z+1] = k
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n-2, arr)