import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = [0] * N
ans = 0

#삽입정렬
for i in range(1, N):
    loc = i
    item = A[i]
    for j in range(i-1, -1, -1):
        if A[j] > item:
            A[j + 1] = A[j]
            loc -= 1
    A[loc] = item

ans = S[0] = A[0]

for i in range(1, N):
    S[i] = S[i-1] + A[i]
    ans += S[i]

print(ans)


