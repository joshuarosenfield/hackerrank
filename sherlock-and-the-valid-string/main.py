#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def isValid(s):
    char_map = Counter(s)
    print(char_map)
    print(char_map.values())
    char_occurence_map = Counter(char_map.values())
    print (char_occurence_map)

    if len(char_occurence_map) == 1:
        return 'YES'
    if len(char_occurence_map) == 2:
        for v in char_occurence_map.values():
            if v == 1:
                return "NO"
    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()


