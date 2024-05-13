T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    A = list(map(int, input().split()))
    dp = [1] * n
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if A[i] <= A[j]:
                dp[j] = max(dp[j], dp[i] + 1)
    
    print(f"#{test_case} {max(dp)}")
