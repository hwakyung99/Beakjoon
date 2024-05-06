for test_case in range(1, 11):
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(2, n-2):
        m = max(h[i-1], h[i-2], h[i+1], h[i+2])
        if m < h[i]:
            ans += h[i] - m
    print(f"#{test_case} {ans}")