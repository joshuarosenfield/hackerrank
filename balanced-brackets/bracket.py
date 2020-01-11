#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    #Each time, when an open parentheses is encountered push it in the stack, and when closed parenthesis is encountered, match it with the top of stack and pop it. If stack is empty at the end, return Balanced otherwise, Unbalanced.
    open_bracket = ["{", "(", "["]
    close_bracket = ["}", ")", "]"]
    b = list(s)
    stack = []
    for i in b:
        if i in open_bracket:
            stack.append(i)
        elif i in close_bracket:
            pos = close_bracket.index(i)
            if((len(stack) > 0) and (open_bracket[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return("NO")
    if len(stack) == 0: 
        return("YES")
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

