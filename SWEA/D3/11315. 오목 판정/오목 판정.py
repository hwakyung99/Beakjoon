def is_omok(x, y, d):
    for _ in range(4):
        x += dxy[d][0]
        y += dxy[d][1]
        check.append([x, y, d])
        if board[x][y] != 'o':
            return False
    return True


T = int(input())
dxy =[(0, 1), (1, 1), (1, 0), (1, -1)]

for test_case in range(1, T + 1):
    n = int(input())
    check = []
    board = []
    ans = False

    for _ in range(n):
        board.append(list(input()))

    for i in range(n):
        if ans:
            break
        for j in range(n):
            if board[i][j] == 'o':
                if n - j >= 5:
                    if [i, j, 0] not in check:
                        check.append([i, j, 0])
                        if is_omok(i, j, 0):
                            ans = True
                            break
                    if n - i >= 5:
                        if [i, j, 1] not in check:
                            check.append([i, j, 1])
                            if is_omok(i, j, 1):
                                ans = True
                                break
                if n - i >= 5:
                    if [i, j, 2] not in check:
                        check.append([i, j, 2])
                        if is_omok(i, j, 2):
                            ans = True
                            break
                    if j >= 4:
                        if [i, j, 3] not in check:
                            check.append([i, j, 3])
                            if is_omok(i, j, 3):
                                ans = True
                                break
    
    if ans:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")
