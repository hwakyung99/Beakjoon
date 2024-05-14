T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    ans = "ON"
    for _ in range(n):
        if m % 2 == 0:
            ans = "OFF"
            break
        m = m // 2
    
    print(f"#{test_case} {ans}")
    