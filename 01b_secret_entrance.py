from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq


pos = 50
ans = 0

with open("input.txt", "r") as file:
    for line in file:
        direc,  moves = line[0], int(line[1:])

        ans += moves//100
        moves %= 100
        
        if direc == 'L':
            moves = -moves

        prev = pos
        
        pos += moves

        if (pos <= 0 or pos >= 100) and prev != 0:
            ans += 1
        
        pos %= 100

        print(f"{line.strip()}----ans, pos = {ans} {pos}")

print(ans)
