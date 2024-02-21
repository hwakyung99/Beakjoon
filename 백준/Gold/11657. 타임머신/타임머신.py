import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
distance = [sys.maxsize] * (N + 1)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))

distance[1] = 0
for _ in range(N - 1):
    for a, b, c in graph:
        if distance[a] != sys.maxsize and distance[b] > distance[a] + c:
            distance[b] = distance[a] + c

for a, b, c in graph:
    if distance[a] != sys.maxsize and distance[b] > distance[a] + c:
        print(-1)
        exit()

for i in range(2, N + 1):
    if distance[i] == sys.maxsize:
        print(-1)
    else:
        print(distance[i])
