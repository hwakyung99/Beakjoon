import sys
input = sys.stdin.readline


def merge_sort(start, end):
    global ans, arr
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)

        p1 = start
        p2 = mid + 1
        tmp = []
        while p1 <= mid and p2 <= end:
            if arr[p1] > arr[p2]:
                ans = ans + (mid + 1) - p1
                tmp.append(arr[p2])
                p2 += 1
            else:
                tmp.append(arr[p1])
                p1 += 1
        if p1 <= mid:
            tmp = tmp + arr[p1:mid + 1]
        if p2 <= end:
            tmp = tmp + arr[p2:end + 1]
        for i in range(len(tmp)):
            arr[start + i] = tmp[i]


N = int(input())
arr = list(map(int, input().split()))
ans = 0

merge_sort(0, N - 1)
print(ans)
