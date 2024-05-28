import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
edge_list = []
distance = [sys.maxsize] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    edge_list.append((A, B))

distance[X] = 0
for _ in range(K):
    for a, b in edge_list:
        if distance[a] != sys.maxsize and distance[b] > distance[a] + 1:
            distance[b] = distance[a] + 1

if distance.count(K) == 0:
    print(-1)
    exit()

for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
