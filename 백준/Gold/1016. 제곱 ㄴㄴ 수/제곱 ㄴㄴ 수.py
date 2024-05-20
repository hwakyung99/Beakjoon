import sys
input = sys.stdin.readline

min_x, max_x = map(int, input().split())

check = [True] * (max_x - min_x + 1)

i = 2
while i * i <= max_x:
    square = i * i

    start = min_x // square
    if min_x % square > 0:
        start += 1

    while square * start <= max_x:
        check[square * start - min_x] = False
        start += 1

    i += 1

print(check.count(True))
