import sys
input = sys.stdin.readline

N = int(input())
s = [0] * (N + 1)
ans = 0

for i in range(1, N + 1):
    s[i] = s[i - 1] + i

p1, p2 = 0, 1
while p1 < N + 1 and p2 < N + 1:
    tmp = s[p2] - s[p1]
    if tmp < N:
        p2 += 1
    elif tmp > N:
        p1 += 1
    else:
        ans += 1
        p1 += 1

print(ans)
