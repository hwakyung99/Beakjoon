T = int(input())

for test_case in range(1, T + 1):
    print(f"#{test_case}", end="")
    n = int(input())
    cnt = [0] * (5001)
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            cnt[i] += 1
    
    p = int(input())
    for _ in range(p):
        c = int(input())
        print(f" {cnt[c]}", end="")
    print()