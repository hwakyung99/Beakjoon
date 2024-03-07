import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline


def dfs(n, c):
    global ans
    if visited[n]:
        return
    if c == 5:
        ans = 1
        return
    visited[n] = True
    for i in G[n]:
        if not visited[i]:
            dfs(i, c + 1)
    visited[n] = False


N, M = map(int, input().split())
G = [[] for _ in range(N)]
visited = [False] * N
ans = 0

for _ in range(M):
    n1, n2 = map(int, input().split())
    G[n1].append(n2)
    G[n2].append(n1)

for j in range(N):
    dfs(j, 1)
    if ans == 1:
        break

print(ans)
