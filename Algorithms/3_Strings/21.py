# https://www.hackerrank.com/challenges/anagram/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s, ans=0):
    if(len(s)%2!=0): return -1
    return sum((Counter(s[:len(s)//2]) - Counter(s[len(s)//2:])).values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()