# https://www.hackerrank.com/challenges/flatland-space-stations/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    return max(c[0], n-c[-1]-1, *[(c[z+1]-c[z])//2 for z in range(len(c)-1)])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, sorted(c))

    fptr.write(str(result) + '\n')

    fptr.close()