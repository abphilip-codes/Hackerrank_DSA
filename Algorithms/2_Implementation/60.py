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
    if(sum([1 for z in set(b) if(z!="_" and b.count(z)==1)])>0): return "NO" 
    if(sum([1 for z in range(1,len(b)-1) if(b.count("_")==0 and b[z] not in [b[z-1],b[z+1]])])>0): return "NO"
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