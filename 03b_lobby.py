from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

ans = 0


def go(battery, ind, start):
    mx = '0'
    best_ind = 0
    for i in range(start, len(battery)-12+1+ind):
        if battery[i] > mx:
            mx = battery[i]
            best_ind = i 

    return mx, best_ind + 1


with open("input.txt", "r") as file:
    for line in file:
        jolt = ''
        line = line.strip()
        start = 0

        for i in range(12):
            digit, start = go(line, i, start)
            jolt += digit

        print(jolt)
        ans += int(jolt)

print(ans)
