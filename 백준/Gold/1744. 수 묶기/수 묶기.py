import sys
input = sys.stdin.readline

N = int(input())
plus = []
minus = []
zero = []
one = 0
ans = 0

for _ in range(N):
    n = int(input())
    if n > 1:
        plus.append(n)
    elif n < 0:
        minus.append(n)
    elif n == 0:
        zero.append(n)
    else:
        one += 1

plus.sort(reverse=True)
minus.sort()

# 양수는 무조건 큰 수부터 묶어서
i = 0
while i < len(plus) - 1:
    ans += plus[i] * plus[i + 1]
    i += 2

if i < len(plus):
    ans += plus[i]

# 음수는 무조건 작은 수부터 묶어서
# 안 묶인 음수는 0의 개수에 따라서 달라짐
i = 0
tmp = []
while i < len(minus) - 1:
    ans += minus[i] * minus[i + 1]
    i += 2

if i < len(minus):
    tmp.append(minus[i])

for j in tmp:
    if zero:
        zero.pop()
    else:
        ans += j

# 1은 곱하지 않고 더하기
ans += one

print(ans)
