import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))
d = deque()

for i in range(N):
    while d and d[-1][1] > A[i]:
        d.pop()
    d.append((i, A[i]))
    while d[0][0] <= d[-1][0] - L:
        d.popleft()
    print(d[0][1], end=' ')
