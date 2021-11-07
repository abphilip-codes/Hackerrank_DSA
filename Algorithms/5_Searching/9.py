# https://www.hackerrank.com/challenges/knightl-on-chessboard/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def knightlOnAChessboard(n):
    def bfs(a,b):
        q,e=deque([(0,0,0)]),{(0,0)}
        while len(q)>0:
            z,y,ans=q.popleft()
            if(z==n-1 and y==n-1): return ans 
            if(z+a<n and y+b<n and (z+a,y+b) not in e):
                e.add((z+a,y+b))
                q.append((z+a,y+b,ans+1))
            if(z+a<n and y-b>=0 and (z+a,y-b) not in e):
                e.add((z+a,y-b))
                q.append((z+a,y-b,ans+1))
            if(z-a>=0 and y+b<n and (z-a,y+b) not in e):
                e.add((z-a,y+b))
                q.append((z-a,y+b,ans+1))
            if(z-a>=0 and y-b>=0 and (z-a,y-b) not in e):
                e.add((z-a,y-b))
                q.append((z-a,y-b,ans+1))
            if(z+b<n and y+a<n and (z+b,y+a) not in e):
                e.add((z+b,y+a))
                q.append((z+b,y+a,ans+1))
            if(z+b<n and y-a>=0 and (z+b,y-a) not in e):
                e.add((z+b,y-a))
                q.append((z+b,y-a,ans+1))
            if(z-b>=0 and y+a<n and (z-b,y+a) not in e):
                e.add((z-b,y+a))
                q.append((z-b,y+a,ans+1))
            if(z-b>=0 and y-a>=0 and (z-b,y-a) not in e):
                e.add((z-b,y-a))
                q.append((z-b,y-a,ans+1))                             
        return -1
    return [[bfs(z,y) for y in range(1,n)] for z in range(1,n)]   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()