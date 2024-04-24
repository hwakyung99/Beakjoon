import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

start = 1
end = N * N
count = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, N + 1):
        count += min(N, mid // i)
    if count >= k:
        end = mid - 1
    else:
        start = mid + 1

print(start)
