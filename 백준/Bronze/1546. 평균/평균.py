import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

max_g = 0
sum_g = 0

for i in range(N):
    if arr[i] > max_g:
        max_g = arr[i]
    sum_g += arr[i]

ans = (sum_g / max_g * 100) / N

print(ans)
