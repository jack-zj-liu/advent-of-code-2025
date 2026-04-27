from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

ans = 0
grid = []

def neis(r, c):
    d = [[0, 1], [0, -1], [1, 1], [1, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1]]
    nei = 0
    for dr, dc in d:
        dr, dc = dr+r, dc+c

        if 0 <= dr < len(grid) and 0 <= dc < len(grid[i]) and grid[dr][dc] == '@':
            nei += 1
    return nei

with open("input.txt", "r") as file:
    for line in file:
        grid.append(list(line.strip()))


    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if neis(i, j) < 4 and grid[i][j] == '@':
                ans += 1

print(ans)
