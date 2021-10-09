# https://www.hackerrank.com/challenges/bear-and-steady-gene/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

def steadyGene(gene):
    a,b,d = 0,0,{'A':0,'T':0,'C':0,'G':0}
    for z in gene: d[z]+=1
    ans=l=len(gene)
    if(d['A']==l/4 and d['T']==l/4 and d['C']==l/4 and d['G']==l/4): return 0
    while a<l and b<l:
        while((d['A']>l/4 or d['C']>l/4 or d['T']>l/4 or d['G']>l/4) and a<l): d[gene[a]],a=d[gene[a]]-1,a+1
        while(d['A']<=l/4 and d['C']<=l/4 and d['T']<=l/4 and d['G']<=l/4): d[gene[b]],b=d[gene[b]]+1,b+1
        ans=min(a-b+1,ans)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()