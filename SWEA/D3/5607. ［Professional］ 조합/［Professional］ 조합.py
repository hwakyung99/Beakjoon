def cal_pow(x, y):
    if y == 1:
        return x % mod
    result = cal_pow(x, y // 2)
    if y % 2 == 0:
        return (result * result) % mod
    else:
        return (result * result * (x % mod)) % mod


mod = 1234567891
max_size = 1000001

factorial = [0] * max_size
factorial[1] = 1
for i in range(2, max_size):
    factorial[i] = (factorial[i-1] * i) % mod

T = int(input())
for test_case in range(1, T + 1):
    n, r = map(int, input().split())
    ans = 1

    a = factorial[n]
    b = (factorial[r] * factorial[n - r]) % mod
    b = cal_pow(b, mod - 2)

    ans = (a * b) % mod
    print(f"#{test_case} {ans}")
