import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
seq = []
ans = []
stack = deque()

for _ in range(n):
    seq.append(int(input()))

i = 0
for j in range(1, n+1):
    stack.append(j)
    ans.append('+')

    while len(stack) > 0 and stack[-1] == seq[i]:
        stack.pop()
        ans.append('-')
        i += 1

if len(stack) > 0:
    print('NO')
else:
    for i in ans:
        print(i)
