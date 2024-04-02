import sys
from collections import deque
input = sys.stdin.readline


def dfs(v):
    check[v] = True
    print(v, end=' ')
    for i in G[v]:
        if not check[i]:
            dfs(i)

def bfs(v):
    q.append(v)
    check[v] = True
    print(v, end=' ')
    while len(q) > 0:
        v = q.popleft()
        for i in G[v]:
            if not check[i]:
                q.append(i)
                check[i] = True
                print(i, end=' ')


N, M, V = map(int, input().split())
G = [[] for _ in range(N + 1)]
check = [False] * (N + 1)
q = deque()

for _ in range(M):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s)

for i in range(1, N + 1):
    G[i].sort()

dfs(V)

print()
check = [False] * (N + 1)

bfs(V)
