# https://www.hackerrank.com/challenges/two-pluses/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid, r=[]):
    for z in range(len(grid)): grid[z] = 'o'+grid[z]+'o'
    grid = ['o'*len(grid[0])]+grid+['o'*len(grid[0])]

    for z in range(1,len(grid)-1):
        for y in range(1,len(grid[0])-1):
            if(grid[z][y]=='G'):
                c,a,s = [(z,y)],1,1
                r.append([a,c.copy()])
                while((grid[z-s][y]=='G') and (grid[z+s][y]=='G') and (grid[z][y-s]=='G') and (grid[z][y+s]=='G')):
                    c.extend([(z-s,y),(z+s,y),(z,y-s),(z,y+s)])
                    a,s=a+4,s+1
                    r.append([a,c.copy()])
        
    return max([r[z][0]*r[y][0] for z in range(len(r)-1) for y in range(z+1,len(r)) if(len(set(r[z][1]).intersection(set(r[y][1])))==0)])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()