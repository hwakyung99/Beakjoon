import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()
for i in B:
    start, mid, end = 0, len(A) // 2, len(A) - 1
    while start <= end:
        if A[mid] == i:
            print(1)
            break
        elif A[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) // 2
    if start > end:
        print(0)
