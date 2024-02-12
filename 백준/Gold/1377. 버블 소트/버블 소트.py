import sys
input = sys.stdin.readline

N = int(input())
arr = []
ans = 0

for i in range(N):
    arr.append((int(input()), i))

arr.sort()

for i in range(N):
    ans = max(ans, arr[i][1] - i)

print(ans + 1)
