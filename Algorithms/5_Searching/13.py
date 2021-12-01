# https://www.hackerrank.com/challenges/count-luck/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#

def printall(k):
    for z in range(len(k)):
        for y in range(len(k[0])):
            print(k[z][y], end=" "*(4 - len(str(k[z][y]))))
        print()
    print()

def countLuck(matrix, k):
    debug = True
    start = end = -1
    dsc = 0
    for z in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[z][y]=='M':
                start = [z,y]
                found = True
            elif matrix[z][y]=='*':
                end = [z,y]
    if debug: printall(matrix)
    if debug: print(start, end)
    dist = [[-1 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    vs = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
    q = deque()
    dist[start[0]][start[1]] = 0
    q.append(start)
    while(len(q)>0):
        cell = q.popleft()
        vs[cell[0]][cell[1]] = True
        nb = [[cell[0]+1, cell[1]], [cell[0]-1, cell[1]], [cell[0], cell[1]+1], [cell[0], cell[1]-1]]
        for n1 in nb:
            x,y = n1
            if(x>-1 and y>-1 and x<len(matrix) and y<len(matrix[0]) and matrix[x][y]!='X' and not(vs[x][y])):
                q.append(n1)
                vs[x][y] = True
                dist[x][y] = dist[cell[0]][cell[1]]+1
    if debug: printall(dist)
    cell = end
    val = dist[end[0]][end[1]]
    while(val!=0):
        nb = [[cell[0]+1, cell[1]], [cell[0]-1, cell[1]], [cell[0], cell[1]+1], [cell[0], cell[1]-1]]
        for n1 in nb:
            x,y = n1
            if(x>-1 and y>-1 and x<len(matrix) and y<len(matrix[0]) and dist[x][y]==dist[cell[0]][cell[1]]-1):
                cell, ct = n1, 0
                val = dist[cell[0]][cell[1]]
                nb = [[cell[0]+1, cell[1]], [cell[0]-1, cell[1]], [cell[0], cell[1]+1], [cell[0], cell[1]-1]]
                ct = 0
                for n1 in nb:
                    x,y = n1
                    if(x>-1 and y>-1 and x<len(matrix) and y<len(matrix[0]) and dist[x][y]==dist[cell[0]][cell[1]]+1): ct += 1
                if(ct>1): dsc +=1
                break
    if dsc == k: return "Impressed"
    return "Oops!"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()