import sys
input = sys.stdin.readline

MAX_N = 100001
N = int(input())
M = int(input())
mate = list(map(int, input().split()))
cnt = [0] * MAX_N
ans = 0

for i in range(N):
    cnt[mate[i]] += 1

for i in range(1, M//2 + 1):
    if i > MAX_N - 1:
        break
    t = M - i
    if t > MAX_N - 1:
        continue
    if i == t:
        ans += cnt[i] // 2
    elif cnt[i] + cnt[t] > 1:
        ans += (cnt[i] + cnt[t]) // 2
if M < MAX_N:
    ans += cnt[M] // 2

print(ans)
