import sys
input = sys.stdin.readline


def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


def dfs(a):
    visited[a] = True
    for b, p, q in graph[a]:
        if not visited[b]:
            recipe[b] = recipe[a] // p * q
            dfs(b)


N = int(input())

recipe = [0] * N
graph = [[] for _ in range(N)]
visited = [False] * N
lcm = 1

for _ in range(N - 1):
    a, b, p, q = map(int, input().split())
    graph[a].append((b, p, q))
    graph[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q))

recipe[0] = lcm
dfs(0)

g = recipe[0]
for i in range(1, N):
    g = gcd(g, recipe[i])

for i in range(N):
    print(recipe[i]//g, end=" ")
