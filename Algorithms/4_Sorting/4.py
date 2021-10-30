# https://www.hackerrank.com/challenges/insertionsort2/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for z in range(1,n):
        k,y=arr[z],z-1
        while(y>=0 and arr[y]>k): arr[y+1],y=arr[y],y-1
        arr[y+1]=k
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)