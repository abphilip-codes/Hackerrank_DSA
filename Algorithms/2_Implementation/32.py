# https://www.hackerrank.com/challenges/almost-sorted/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    z,k,t,s=0,[],arr,sorted(arr)
    if(arr==s): return "yes"
    for a,b in zip(arr,s):
        if(a!=b): k.append((a,z))
        z+=1
    if(len(k)==2):
        t[k[0][1]],t[k[1][1]] = k[1][0],k[0][0]
        if(t==s): return "yes\nswap "+str(k[0][1]+1)+" "+str(k[1][1]+1)
    if(arr[:k[0][1]]+arr[k[0][1]:k[-1][1]+1][::-1]+arr[k[-1][1]+1:]!=s): return "no"
    return "yes\nreverse "+str(k[0][1]+1)+" "+str(k[-1][1]+1)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(almostSorted(arr))