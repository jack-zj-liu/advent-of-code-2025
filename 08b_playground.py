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

adj = defaultdict(list)

def dist(i, j):
    return (boxes[i][0] - boxes[j][0])**2 + (boxes[i][1] - boxes[j][1])**2 + (boxes[i][2] - boxes[j][2])**2

with open("input.txt", "r") as file:
    for line in file:
        box = line.strip().split(',')
        boxes.append((int(box[0]), int(box[1]), int(box[2])))

mndists = []

parent = {i: i for i in range(len(boxes))}

for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        heapq.heappush(mndists, (dist(i, j), i, j))

def find(i):
    p = parent[i]
    while p != parent[p]:
        p = parent[p]
    return p

groups = len(boxes)

while mndists:
    d, i, j = heapq.heappop(mndists)

    if find(i) != find(j):
        groups -= 1
        if groups == 1:
            print(boxes[i][0] * boxes[j][0])
            break

        parent[find(i)] = j


    