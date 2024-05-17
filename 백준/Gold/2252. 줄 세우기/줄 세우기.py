import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
edges = [0] * (N + 1)
q = deque()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    edges[b] += 1

for i in range(1, N + 1):
    if edges[i] == 0:
        q.append(i)

while q:
    n = q.popleft()
    print(n, end=" ")
    for i in graph[n]:
        edges[i] -= 1
        if edges[i] == 0:
            q.append(i)
            