# https://www.hackerrank.com/challenges/maximum-palindromes/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

def initialize(s, M=1000000007):
    arr = [[0 for _ in range(len(s)+1)] for _ in range(26)]
    for z in range(len(s)):
        for y in range(26): arr[y][z+1] = arr[y][z]+((ord(s[z])-97)==y)
    f,m = [1]*(len(s)+1),[1]*(len(s)+1)
    for z in range(1,len(s)+1):
        f[z] = (f[z-1]*z) % M
        m[z] = pow(f[z], M-2, M)
    return arr, f, m

#
# Complete the 'answerQuery' function below.
# Return the answer for this query modulo 1000000007.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def answerQuery(l, r, arr, f, m, M=1000000007):
    o,e,d = 0,0,1
    for z in range(26):
        k = arr[z][r] - arr[z][l-1]
        o,e,d = o+(k&1), e+(k//2), (d*m[k//2])%M
    return (max(o,1)*f[e]*d)%M

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    arr, f, m = initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r, arr, f, m)

        fptr.write(str(result) + '\n')

    fptr.close()