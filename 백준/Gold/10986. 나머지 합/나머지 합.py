import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m
ans = 0

S[0] = A[0] % m
C[S[0]] += 1
for i in range(1, n):
    S[i] = (S[i-1] + A[i]) % m
    C[S[i]] += 1

ans += C[0]
for i in range(m):
    ans += C[i] * (C[i] - 1) / 2

print(int(ans))