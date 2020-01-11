#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag_dict = {}
    note_dict = {}
    for item in magazine:
        if item in mag_dict:
            mag_dict[item] += 1
        else:
            mag_dict[item] = 1
    for item in note:
        if item in note_dict:
            note_dict[item] += 1
        else:
            note_dict[item] = 1

    for item in note_dict:
        if item in mag_dict:
            if mag_dict[item] >= note_dict[item]:
                pass
            else:
                print("No")
                return
        else:
            print("No")
            return
    print("Yes")
    
    #     print(item)
    # print(mag_dict)
    # print(note_dict)

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

