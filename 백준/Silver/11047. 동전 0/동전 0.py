import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
start, end, mid = 0, N - 1, 0
ans = 0

for _ in range(N):
    coin.append(int(input()))

while start < end:
    mid = (start + end) // 2
    if coin[mid] <= K:
        start = mid + 1
    else:
        end = mid - 1

while K != 0:
    ans += K // coin[start]
    K %= coin[start]
    start -= 1

print(ans)
