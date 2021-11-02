# https://www.hackerrank.com/challenges/insertion-sort/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def add(arr, L, R):
    y = l = r = z = 0
    ll,rr = len(L),len(R)
    while(l<ll and r<rr):
        if (L[l]<=R[r]): arr[y],l = L[l],l+1
        else: arr[y],r,z = R[r],r+1,z+ll-l
        y+=1
    while(l<ll): arr[y],l,y = L[l],l+1,y+1
    while(r<rr): arr[y],r,y = R[r],r+1,y+1
    return z

def insertionSort(arr, z=0):
    m = len(arr)//2
    if(m>0):
        L = arr[:m]
        R = arr[m:]        
        z += insertionSort(L)
        z += insertionSort(R)
        z += add(arr,L,R)
    return z

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()