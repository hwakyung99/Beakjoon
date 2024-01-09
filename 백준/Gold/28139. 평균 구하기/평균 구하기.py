import sys, math
input = sys.stdin.readline


def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)


N = int(input())
pos = []
for _ in range(N):
    x, y = map(int, input().split())
    pos.append((x, y))

s = 0
for i in range(N):
    for j in range(i + 1, N):
        s = s + distance(pos[i], pos[j])

print(s * 2 / N)
