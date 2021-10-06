# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(y):
    if (y==1918): return '26.09.{}'.format(y)
    elif ((y<=1917) and (y%4==0)) or ((y>1918) and (y%400==0 or ((y%4==0) and (year%100!=0)))): return '12.09.{}'.format(y)
    else: return '13.09.{}'.format(y)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()