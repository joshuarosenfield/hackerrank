#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ret = 0
    # Creating an empty dictionary  
    freq = {} 
    for item in ar: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    for key, value in freq.items():
        print ("% d : % d"%(key, value))
        ret += value // 2;
    return ret
        # print ("% d : % d"%(key, value)) 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

