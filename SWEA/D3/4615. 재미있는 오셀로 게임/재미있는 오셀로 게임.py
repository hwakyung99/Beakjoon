def change(x, y, stone):
    board[x][y] = stone
    lst = []

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        while True:
            if -1 < nx < n and -1 < ny < n:
                if board[nx][ny] == stone:
                    while lst:
                        tmp = lst.pop()
                        board[tmp[0]][tmp[1]] = stone
                    break
                elif board[nx][ny] == 0:
                    lst.clear()
                    break
                else:
                    lst.append([nx, ny])
            else:
                lst.clear()
                break
            nx += dx[i]
            ny += dy[i]


T = int(input())

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    cnt_b, cnt_w = 0, 0
    s = n // 2 - 1
    board[s][s], board[s + 1][s + 1], board[s][s + 1], board[s + 1][s] = 2, 2, 1, 1

    for _ in range(m):
        x, y, stone = map(int, input().split())
        change(x - 1, y - 1, stone)

    for i in range(n):
        cnt_b += board[i].count(1)
        cnt_w += board[i].count(2)

    print(f"#{test_case} {cnt_b} {cnt_w}")
