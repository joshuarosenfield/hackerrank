#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    ret = []
    for i in range(4):
        for l in range(4):
            total = arr[i][l] + arr[i][l+1] + arr[i][l+2] + arr[i+1][l+1] + arr[i+2][l] + arr[i+2][l+1] + arr[i+2][l+2]  
            ret.append(total)
    return(max(ret))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

