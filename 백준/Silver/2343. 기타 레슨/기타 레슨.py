import sys
input = sys.stdin.readline

N, M = map(int, input().split())
course = list(map(int, input().split()))

start = max(course)
end = sum(course)
mid = (start + end) // 2

ans = end

while start <= end:
    mid = (start + end) // 2
    # if mid < max(course):
    #     start = mid + 1
    #     continue
    total = 0
    count = 1
    for i in course:
        if total + i <= mid:
            total += i
        else:
            total = i
            count += 1
    if count <= M:
        end = mid - 1
        ans = min(ans, mid)
    else:
        start = mid + 1

print(ans)
