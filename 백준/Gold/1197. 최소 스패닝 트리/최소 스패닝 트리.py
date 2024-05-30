import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
pq = []
mst = 0

for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

heapq.heappush(pq, (0, 1))

while pq:
    w, e = heapq.heappop(pq)
    if visited[e]:
        continue
    mst += w
    visited[e] = True
    for n_e, n_w in graph[e]:
        if not visited[n_e]:
            heapq.heappush(pq, (n_w, n_e))

print(mst)
