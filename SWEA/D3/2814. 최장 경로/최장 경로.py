def dfs(v, cnt):
    global ans

    ans = max(ans, cnt)
    visited[v] = True
    for e in graph[v]:
        if not visited[e]:
            dfs(e, cnt + 1)
    visited[v] = False


T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    cnt = 0
    ans = 0
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, cnt + 1)

    print(f"#{test_case} {ans}")