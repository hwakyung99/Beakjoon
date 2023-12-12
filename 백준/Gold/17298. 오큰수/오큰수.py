import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
stack = []
ans = [0]*N

for i in range(N - 1, -1, -1):
    while stack and A[i] >= stack[-1]:
        stack.pop()
    if stack and A[i] < stack[-1]:
        ans[i] = stack[-1]
    else:
        ans[i] = -1
    stack.append(A[i])

print(*ans)