import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

for k in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            dist[s][e] = min(dist[s][e], dist[s][k] + dist[k][e])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
