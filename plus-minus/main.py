#!/bin/python3

import math
import os
import random
import re
import sys
import decimal

# Complete the plusMinus function below.
def plusMinus(arr):
    pos, neg, zero = 0, 0, 0
    for x in arr:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zero += 1

    pos = pos / len(arr)
    neg = neg / len(arr)
    zero = zero / len(arr)

    print ('%.6f'%pos)
    print ('%.6f'%neg)
    print ('%.6f'%zero)
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

