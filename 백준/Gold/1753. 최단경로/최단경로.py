import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
g = [[] for _ in range(V + 1)]
distance = [sys.maxsize] * (V + 1)
visited = [False] * (V + 1)
q =[]

for _ in range(E):
    u, v, w = map(int, input().split())
    g[u].append((v, w))

distance[K] = 0
heapq.heappush(q, (0, K))

while len(q) > 0:
    c = heapq.heappop(q)
    c_v = c[1]
    for n in g[c_v]:
        n_v = n[0]
        n_w = n[1]
        if distance[c_v] + n_w < distance[n_v]:
            distance[n_v] = distance[c_v] + n_w
            heapq.heappush(q, (distance[n_v], n_v))

for i in range(1, V + 1):
    if distance[i] == sys.maxsize:
        print('INF')
    else:
        print(distance[i])
