def adjacent(r):
    for i in range(r):
        if row[i] == row[r] or abs(i - r) == abs(row[i] - row[r]):  # 같은 열, 대각선에 있는가
            return False
    return True


def dfs(r):
    global ans
    if r == n:
        ans += 1
        return
    for c in range(n):
        row[r] = c  # r번째 행 c번째 열에 퀸을 놓음
        if adjacent(r):  # 놓을 수 있는지 확인
            dfs(r + 1)  # 놓을 수 있으면 다음 행으로
        row[r] = -1  # 놓을 수 없거나 함수 복귀 후 빼기


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    ans = 0
    row = [-1] * n

    dfs(0)

    print(f"#{test_case} {ans}")
