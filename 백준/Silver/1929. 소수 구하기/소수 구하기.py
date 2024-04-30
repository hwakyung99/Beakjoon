import sys, math
input = sys.stdin.readline

M, N = map(int, input().split())


for i in range(M, N + 1):
    if i == 1:
        continue
    prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            if i != j:
                prime = False
                break
    if prime:
        print(i)
