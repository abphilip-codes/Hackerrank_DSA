# https://www.hackerrank.com/challenges/3d-surface-area/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    x = [[0]*(len(A[0])+2)]+[[0]+z+[0] for z in A]+[[0]*(len(A[0])+2)]
    ans = [abs(x[z][y]-x[z-1][y])+abs(x[z][y]-x[z][y-1]) for z in range(1,len(x)) for y in range(1,len(x[z]))]
    return sum(ans)+(len(A)*len(A[0])*2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()