import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))
s = [0] * (N + 1)

s[1] = nums[1]
for i in range(2, N + 1):
    s[i] = s[i-1] + nums[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(s[j] - s[i - 1])
