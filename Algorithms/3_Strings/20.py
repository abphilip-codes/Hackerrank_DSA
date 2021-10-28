# https://www.hackerrank.com/challenges/palindrome-index/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    for p in range(len(s)//2+1):
        q = len(s) - p - 1
        if s[p] != s[~p]:
            if s[p+1:q+1] == s[q:p:-1]: return p
            elif s[p:q] == s[p:q][::-1]: return q
            else: return -1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()