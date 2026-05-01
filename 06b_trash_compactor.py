from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

grid = []
width = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line[:-1]
        width = max(width, len(line))
        grid.append(line)

for i in range(len(grid)):
    if len(grid[i]) < width:
        grid[i] += ' ' * (width - len(grid[i]))

ans = 0
nums = []


for j in range(len(grid[0])-1, -1, -1):
    curr = ''
    for i in range(len(grid)):
        curr += grid[i][j]

    if curr[-1] == '*':
        nums.append(curr[:-1])
        p = 1
        for num in nums:
            p *= int(num)
        ans += p
        nums.clear()
    elif curr[-1] == '+':
        nums.append(curr[:-1])
        for num in nums:
            ans += int(num)
        nums.clear()
        
    else:
        if curr.strip() != '':
            nums.append(curr)

print(ans)
