# https://www.hackerrank.com/challenges/runningtime/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(n, arr):
    return len([1 for z in range(n) for y in range(z,n) if(arr[z]>arr[y])])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()