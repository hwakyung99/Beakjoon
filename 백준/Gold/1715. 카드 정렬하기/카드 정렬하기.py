import sys
import heapq
input = sys.stdin.readline

N = int(input())
ans = 0
heap = []

for _ in range(N):
    heapq.heappush(heap, int(input()))

while len(heap) > 1:
    s = heapq.heappop(heap) + heapq.heappop(heap)
    ans += s
    heapq.heappush(heap, s)

print(ans)
