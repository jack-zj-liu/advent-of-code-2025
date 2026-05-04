from sys import stdin
from functools import cache
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

boxes = []
ans = []
connections = 1000

adj = defaultdict(list)

def dist(i, j):
    return (boxes[i][0] - boxes[j][0])**2 + (boxes[i][1] - boxes[j][1])**2 + (boxes[i][2] - boxes[j][2])**2

with open("input.txt", "r") as file:
    for line in file:
        box = line.strip().split(',')
        boxes.append((int(box[0]), int(box[1]), int(box[2])))

mndists = []

for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        heapq.heappush(mndists, (-dist(i, j), i, j))
        if len(mndists) > connections:
            heapq.heappop(mndists)

for d, i, j in mndists:
    adj[i].append(j)
    adj[j].append(i)

seen = set()

def dfs(b):
    sz = 1
    seen.add(b)
    for nei in adj[b]:
        if nei not in seen:
            sz += dfs(nei)
    return sz

for i in range(len(boxes)):
    if i not in seen:
        ans.append(dfs(i))

ans.sort()
print(ans[-1] * ans[-2] * ans[-3])
