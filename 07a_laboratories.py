from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

grid = []
ans = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        grid.append(list(line))

for i in range(len(grid)-1):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S' or grid[i][j] == '|':
            if grid[i+1][j] == '^':
                if j-1>=0: grid[i+1][j-1] = '|'
                if j+1 < len(grid[0]): grid[i+1][j+1] = '|'
                ans += 1
            else:
                grid[i+1][j] = '|'

print(ans)
