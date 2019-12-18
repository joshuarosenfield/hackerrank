#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_total = Counter(a)
    b_total = Counter(b)
    a_total.subtract(b_total)
    return sum(abs(i) for i in a_total.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

