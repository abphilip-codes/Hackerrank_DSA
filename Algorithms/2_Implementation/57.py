# https://www.hackerrank.com/challenges/fair-rations/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    B = [z for z,y in enumerate(B) if(y%2)]
    return "NO" if(len(B)%2) else str(sum([(B[z+1]-B[z])*2 for z in range(0,len(B),2)]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()