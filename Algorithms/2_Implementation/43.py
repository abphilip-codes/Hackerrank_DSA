# https://www.hackerrank.com/challenges/acm-icpc-team/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import time

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    l,d = [set([z for z in range(len(y)) if y[z]=='1']) for y in topic],{}
    for z in range(len(l)-1):
        for y in range(z+1,len(l)): d[len(l[z].union(l[y]))]=d.get(len(l[z].union(l[y])),0)+1
    return [max(d.keys()),d[max(d.keys())]]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()