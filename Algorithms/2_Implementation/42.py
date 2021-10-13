# https://www.hackerrank.com/challenges/queens-attack-2/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    l,ans = set([(x,y) for x,y in obstacles]),0
    for z in [[-1, 1],[0, 1],[1, 1],[-1, 0],[1, 0],[-1,-1],[0,-1],[1,-1]]:
        x,y = r_q+z[0],c_q+z[1]
        while (x not in [0,n+1] and y not in [0,n+1]) and (x,y) not in l:
            ans,x,y=ans+1,x+z[0],y+z[1]
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()