import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ans = 0

A.sort()

for i in range(N):
    l, r = 0, N - 1
    while l < r:
        tmp = A[l] + A[r]
        if l == i:
            l += 1
        elif r == i:
            r -= 1
        elif tmp == A[i]:
            ans += 1
            break
        elif tmp > A[i]:
            r -= 1
        elif tmp < A[i]:
            l += 1

print(ans)
