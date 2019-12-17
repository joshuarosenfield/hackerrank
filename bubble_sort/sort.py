#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    n = len(a)
    swap = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                swap += 1
                a[j], a[j+1] = a[j+1], a[j]
    print("Array is sorted in " + str(swap) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[len(a)-1]))
    
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

