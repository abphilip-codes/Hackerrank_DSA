# https://www.hackerrank.com/challenges/happy-ladybugs/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    for a in set(b):
        if a != "_" and b.count(a) == 1: return "NO"
    
    if b.count("_") == 0:
        for i in range(1,n-1):
            if b[i-1]!=b[i] and b[i+1]!=b[i]: return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()