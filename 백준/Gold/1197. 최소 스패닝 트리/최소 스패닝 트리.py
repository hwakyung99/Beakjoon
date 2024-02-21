import sys
import heapq
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x


V, E = map(int, input().split())
graph = []
parent = [i for i in range(V + 1)]
mst = 0

for _ in range(E):
    A, B, C = map(int, input().split())
    heapq.heappush(graph, (C, A, B))

i = 0
while i < V - 1:
    c, a, b = heapq.heappop(graph)
    if find(a) != find(b):
        union(a, b)
        mst += c
        i += 1

print(mst)
