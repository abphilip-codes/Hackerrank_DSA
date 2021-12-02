# https://www.hackerrank.com/challenges/red-knights-shortest-path/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'printShortestPath' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER i_start
#  3. INTEGER j_start
#  4. INTEGER i_end
#  5. INTEGER j_end
#

def printShortestPath(n,IS,JS,IE,JE):
    D,K = ((-1,-2),(1,-2),(2,0),(1,2),(-1,2),(-2,0)),[]
    A = {z:y for z,y in zip(D,("UL","UR","R","LR","LL","L"))}
    if(abs(JS-JE)%2*2==abs(IS-IE)%4):
        while((JS,IS)!=(JE,IE)):
            JS,IS,n = min(((JS+z,IS+y,(z,y)) for z,y in D),
                        key=lambda x:abs(JE-x[0])+abs(IE-x[1]))
            K+=[n]
        print(len(K))
        print(*(A[z] for z in sorted(K, key=lambda x:D.index(x))))
    else: print("Impossible")

if __name__ == '__main__':
    n = int(input().strip())

    first_multiple_input = input().rstrip().split()

    i_start = int(first_multiple_input[0])

    j_start = int(first_multiple_input[1])

    i_end = int(first_multiple_input[2])

    j_end = int(first_multiple_input[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)