# https://www.hackerrank.com/challenges/cavity-map/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(g):
    for z in range(1,len(g)-1):
        for y in range(1,len(g)-1):
            if g[z][y] > max(g[z-1][y],g[z+1][y],g[z][y-1],g[z][y+1]):
                g[z] = g[z][:y]+'X'+g[z][y+1:]
    return g

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()