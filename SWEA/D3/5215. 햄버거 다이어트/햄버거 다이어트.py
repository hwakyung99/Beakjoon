T = int(input())


def dfs(i, l, s):
    global ans, N

    if l < 0:
        return
    if i == N:
        ans = max(ans, s)
        return
    dfs(i + 1, l - kcal[i], s + score[i])
    dfs(i + 1, l, s)


for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    score = []
    kcal = []
    for _ in range(N):
        S, K = map(int, input().split())
        score.append(S)
        kcal.append(K)

    ans = 0
    total = 0

    dfs(0, L, 0)

    print("#{} {}".format(test_case, ans))
