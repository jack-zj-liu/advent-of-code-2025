from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

ans = 0
grid = []
ready = deque()
num_neis = Counter()
d = [[0, 1], [0, -1], [1, 1], [1, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1]]
seen = set()

def neis(r, c):
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
            num_neis[(i, j)] = neis(i, j)
            if num_neis[(i, j)] < 4 and grid[i][j] == '@':
                ready.append((i, j))
                seen.add((i, j))
    
    while ready:
        r, c = ready.popleft()
        for dr, dc in d:
            dr, dc = dr+r, dc+c
            if 0 <= dr < len(grid) and 0 <= dc < len(grid[0]) and grid[dr][dc] == '@':
                num_neis[(dr, dc)] -= 1
                if (dr, dc) not in seen and num_neis[(dr, dc)] < 4:
                    ready.append((dr, dc))
                    seen.add((dr, dc))
        ans += 1

print(ans)
