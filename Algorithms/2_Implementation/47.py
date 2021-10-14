# https://www.hackerrank.com/challenges/bigger-is-greater/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    w=list(w)
    for z in range(len(w)-2,-1,-1):
        for y in range(z+1,len(w)):
            if w[z]<w[y]:
                w[z],w[y]=w[y],w[z]
                return "".join(w)      
        else: w[z:]=sorted(w[z:])
    return 'no answer'   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()