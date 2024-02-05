import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
d = deque()
t = False

for i in range(1, N+1):
    d.append(i)

while len(d) > 1:
    if t:
        d.append(d[0])
    d.popleft()
    t = not t

print(d[0])
