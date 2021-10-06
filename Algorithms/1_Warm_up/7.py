# https://www.hackerrank.com/challenges/staircase/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
    space = ""
    h = ""
    for i in range(1,n+1):
        for j in range(i,n): space=space+" "
        for j in range(0,i): h=h+"#"
        print(space+h)
        space = ""
        h = ""

if __name__ == '__main__':
    n = int(input())
    staircase(n)