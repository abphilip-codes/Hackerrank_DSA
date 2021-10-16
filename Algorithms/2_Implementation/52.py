# https://www.hackerrank.com/challenges/the-time-in-words/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    n =['','one','two','three','four','five','six','seven',
       'eight','nine','ten','eleven','twelve','thirteen','fourteen',
       'quarter','sixteen','seventeen','eighteen','nineteen', 'twenty',
       'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five',
       'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']
       
    if m==0: return n[h]+' o\' clock'
    elif m>30: 
        if(m==45): return 'quarter to '+n[h+1]  
        elif(m==59): return n[(60-m)]+' minute to '+n[h+1]
        else: return n[(60-m)]+' minutes to '+n[h+1]
    elif m<30: 
        if(m==15): return 'quarter past '+n[h]  
        elif(m==1): return n[m]+' minute past '+n[h]
        else: return n[m]+' minutes past '+n[h]
    else: return 'half past '+n[h]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()