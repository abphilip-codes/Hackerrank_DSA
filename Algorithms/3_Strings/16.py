# https://www.hackerrank.com/challenges/funny-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s,r):
    a = [abs(ord(s[z+1])-ord(s[z])) for z in range(len(s)-1)]
    b = [abs(ord(r[z+1])-ord(r[z])) for z in range(len(r)-1)]
    return "Funny" if(a==b) else "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        
        r = list(reversed(s))
        
        result = funnyString(s,r)

        fptr.write(result + '\n')

    fptr.close()