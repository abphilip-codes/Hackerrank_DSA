# https://www.hackerrank.com/challenges/xor-quadruples/problem

#!/bin/python3

import os
import sys

#
# Complete the beautifulQuadruples function below.
#

def beautifulQuadruples(a, b, c, d):
    a,b,c,d = sorted([a,b,c,d])
    k,t,ans = [0]*(2**len('{:b}'.format(d))),0,0
    for z in range(c): 
        for y in range(z,d): k[(z+1)^(y+1)],t = k[(z+1)^(y+1)]+1,t+1
    for z in range(b):
        for y in range(min(a,z+1)): ans+=(t-k[(z+1)^(y+1)])
        for y in range(z,d): k[(z+1)^(y+1)],t = k[(z+1)^(y+1)]-1,t-1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    abcd = input().split()

    a = int(abcd[0])

    b = int(abcd[1])

    c = int(abcd[2])

    d = int(abcd[3])

    result = beautifulQuadruples(a, b, c, d)

    fptr.write(str(result) + '\n')

    fptr.close()