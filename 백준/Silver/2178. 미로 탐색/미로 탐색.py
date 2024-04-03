import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    d.append((x, y))
    while d:
        x, y = d.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if N > nx > -1 and M > ny > -1 and maze[nx][ny] == 1:
                d.append((nx, ny))
                maze[nx][ny] += maze[x][y]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
maze = []
d = deque()

for _ in range(N):
    maze.append(list(map(int, input().strip())))

bfs(0, 0)
print(maze[N - 1][M - 1])
