# https://www.hackerrank.com/challenges/append-and-delete/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k, z=0):
    while(z<=min(len(s),len(t)) and s[:z]==t[:z]): n,z=len(s)+len(t)-2*z,z+1
    return 'Yes' if((n+2*(z-1))<k or (n<=k and (k-n)%2==0)) else 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()