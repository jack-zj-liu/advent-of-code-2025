from sys import stdin
from functools import cache
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

grid = []
ans = 0

@cache
def go(r, c):
    print(r, c)
    if r == len(grid)-1:
        return 1

    if grid[r+1][c] == '^':
        return go(r+1, c+1) + go(r+1, c-1)
    else:
        return go(r+1, c)

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        grid.append(list(line))

for j in range(len(grid[0])):
    if grid[0][j] == 'S':
        sc = j
        break

ans = go(0, sc)

print(ans)
