import sys
input = sys.stdin.readline

A, B = map(int, input().split())
a = max(A, B)
b = min(A, B)
mod = a % b

while mod != 0:
    tmp = mod
    mod = b % mod
    b = tmp

for _ in range(b):
    print(1, end='')
