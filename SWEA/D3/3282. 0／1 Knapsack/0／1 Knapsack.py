T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        v, c = map(int, input().split())
        for j in range(k + 1):
            if j >= v:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - v] + c)
            else:
                dp[i][j] = dp[i - 1][j]
    
    print(f"#{test_case} {dp[n - 1][k]}")