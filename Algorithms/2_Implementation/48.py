# https://www.hackerrank.com/challenges/kaprekar-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    ans=[z for z in range(p,q+1) if((z**2)//10**len(str(z))+(z**2)%10**len(str(z))==z)]
    print(*ans) if(ans) else print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)