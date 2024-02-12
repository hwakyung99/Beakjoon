import sys
input = sys.stdin.readline


def dfs(n):
    global N
    stack.append(n)
    visited[n] = 1
    while len(stack) != 0:
        v = stack.pop()
        for j in range(1, N + 1):
            if g[v][j] == 1:        # 인접노드인지
                if visited[j] == 0:     # 방문했는지
                    stack.append(j)
                    visited[j] = 1


N, M = map(int, input().split())
g = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
stack = []
ans = 0

for _ in range(M):
    n1, n2 = map(int, input().split())
    g[n1][n2] = g[n2][n1] = 1

for i in range(1, N+1):
    if visited[i] == 0:
        if len(stack) == 0:
            ans += 1
        dfs(i)

print(ans)
