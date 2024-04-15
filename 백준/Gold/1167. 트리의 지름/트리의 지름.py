import sys
input = sys.stdin.readline


def dfs(e, w):
    global max_v, max_i
    if visited[e]:
        return
    if w > max_v:
        max_v = w
        max_i = e
    visited[e] = True
    for ne, nw in tree[e]:
        if not visited[ne]:
            dfs(ne, w + nw)


V = int(input())
tree = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
max_v = 0
max_i = 0

for _ in range(1, V + 1):
    edges = list(map(int, input().split()))
    for j in range(1, len(edges)-1, 2):
        E, W = edges[j:j + 2]
        tree[edges[0]].append((E, W))

dfs(1, 0)

visited = [False] * (V + 1)
max_v = 0
dfs(max_i, 0)

print(max_v)