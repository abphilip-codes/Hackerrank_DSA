# https://www.hackerrank.com/challenges/quicksort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr, k=0):
    for z in range(len(arr)):
        if(arr[z]<arr[k]): arr,k = arr[:k]+arr[z:z+1]+arr[k:z]+arr[z+1:],k+1
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()