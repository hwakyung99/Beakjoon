T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    half = n // 2
    ans = 0

    for i in range(n):
        arr = list(map(int, input().strip()))
        diff = abs(i - half)
        if diff == 0:
            ans += sum(arr)
        else:
            ans += sum(arr[diff:-diff])

    print(f"#{test_case} {ans}")
