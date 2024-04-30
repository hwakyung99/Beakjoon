import sys
import heapq
input = sys.stdin.readline

heap = []
ans = 0

N = int(input())

for _ in range(N):
    s, e = map(int, input().split())
    heapq.heappush(heap, (e, s))    # 끝나는 시간을 기준으로 정렬

pre = 0  # 이전 강의 끝난 시간
while heap:
    I = heapq.heappop(heap)
    if pre <= I[1]:
        ans += 1
        pre = I[0]

print(ans)
