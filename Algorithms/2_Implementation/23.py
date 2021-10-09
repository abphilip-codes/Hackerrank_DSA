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

def matrixRotation(m, t):
    r = len(m)
    c = len(m[0])
    for z in range(min(r,c)//2):
        ans = (m[z][z:c-z] + [m[k][-1-z] for k in range(z+1,r-1-z)] + 
               m[-1-z][z:c-z][::-1] + [m[k][z] for k in range(r-2-z,z,-1)])
        ans = ans[t%len(ans):]+ans[:t%len(ans)]
        for y in range(z,c-z): m[z][y] = ans.pop(0)
        for y in range(z+1,r-z-1): m[y][-1-z] = ans.pop(0)
        for y in range(c-z-1,z-1,-1): m[-1-z][y] = ans.pop(0)
        for y in range(r-z-2,z,-1): m[y][z] = ans.pop(0)
    for k in m: print(*k)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)