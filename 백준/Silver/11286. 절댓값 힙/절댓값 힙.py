import sys
import heapq

input = sys.stdin.readline

N = int(input())
h = []

for _ in range(N):
    item = int(input())
    if item == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(item), item))
