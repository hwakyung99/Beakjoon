import sys
input = sys.stdin.readline

n = int(input())
ans = n

i = 2
while i*i <= n:
    if n % i == 0:
        while n % i == 0:
            n //= i
        ans *= (1 - 1 / i)
    i += 1

if n > 1:
    ans *= (1 - 1 / n)

print(int(ans))
