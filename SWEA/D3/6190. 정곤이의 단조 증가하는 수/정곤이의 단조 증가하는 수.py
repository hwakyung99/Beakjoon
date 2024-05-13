def is_dan(num):
    if num // 10 == 0 or num % 10 == 0:
        return False

    remain = num % 10
    num = num // 10
    while num > 0:
        if num % 10 > remain:
            return False
        remain = num % 10
        num = num // 10
    return True


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    A = list(map(int, input().split()))
    ans = -1

    for i in range(n - 1):
        for j in range(i + 1, n):
            tmp = A[i] * A[j]
            if tmp > ans and is_dan(tmp):
                ans = tmp

    print(f"#{test_case} {ans}")
