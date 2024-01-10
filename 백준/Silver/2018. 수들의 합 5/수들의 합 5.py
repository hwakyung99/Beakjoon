import sys
input = sys.stdin.readline

N = int(input())
l, r, s, ans = 1, 1, 1, 0

while l < N + 1 and r < N + 1:
    if s < N:
        r += 1
        s += r
    elif s > N:
        s -= l
        l += 1
    else:
        ans += 1
        s -= l
        l += 1

print(ans)
