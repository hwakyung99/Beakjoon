import sys, math
input = sys.stdin.readline

A, B = map(int, input().split())

prime = [True] * (int(math.sqrt(B)) + 1)
prime[0], prime[1] = False, False
ans = 0

for i in range(2, int(math.sqrt(B)) + 1):
    if prime[i]:
        for j in range(2 * i, int(math.sqrt(B)) + 1, i):
            prime[j] = False

for i in range(2, int(math.sqrt(B)) + 1):
    if prime[i]:
        tmp = i * i
        while tmp <= B:
            if tmp >= A:
                ans += 1
            tmp *= i

print(ans)
