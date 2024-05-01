import sys, math
input = sys.stdin.readline

MAX = 2000001
N = int(input())

prime = [False, False] + [True] * (MAX - 2)


for i in range(2, MAX):
    if prime[i]:
        for j in range(2 * i, MAX, i):
            prime[j] = False

for i in range(N, MAX):
    if prime[i]:
        palindrome = True
        p = str(i)
        l, r = 0, len(p) - 1
        while l <= r:
            if p[l] != p[r]:
                palindrome = False
                break
            l += 1
            r -= 1
        if palindrome:
            print(p)
            break
