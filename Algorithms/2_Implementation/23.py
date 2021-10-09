# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, rotation):
    r = len(matrix)
    c = len(matrix[0])
    layerCount = min(r,c)//2
    layer = []
    for i in range(layerCount):
        circle = []
        circle += matrix[i][i:c-i]
        circle += [matrix[k][-1-i] for k in range(i+1,r-1-i)]
        circle += matrix[-1-i][i:c-i][::-1]
        circle += [matrix[k][i] for k in range(r-2-i,i,-1)]
        ro = rotation % len(circle)
        circle = circle[ro:]+circle[:ro]
        cnt = 0
        # print(circle)
        for idx in range(i,c-i):
            matrix[i][idx] = circle[cnt]
            cnt+=1
        for idx in range(i+1,r-1-i):
            matrix[idx][-1-i] = circle[cnt]
            cnt+=1
        for idx in range(c-i-1, i-1,-1):
            matrix[-1-i][idx] = circle[cnt]
            cnt+=1
        for idx in range(r-2-i,i,-1):
            matrix[idx][i]=circle[cnt]
            cnt+=1
    for m in matrix:
        print(' '.join(list(map(str,m))))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)