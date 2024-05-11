def dfs(i, t):
    global ans
    if i == n or t >= k:
        if t == k:
            ans += 1
        return
    dfs(i + 1, t + A[i])
    dfs(i + 1, t)


T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0

    dfs(0, 0)

    print("#{} {}" .format(test_case, ans))
