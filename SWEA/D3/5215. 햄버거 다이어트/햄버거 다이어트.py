T = int(input())


def dfs(i, l):
    global ans, total

    for j in range(i, N):
        if l - arr[j][1] >= 0:
            total += arr[j][0]
            ans = max(ans, total)
            dfs(j + 1, l - arr[j][1])
            total -= arr[j][0]


for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    ans = 0
    total = 0

    dfs(0, L)

    print("#{} {}".format(test_case, ans))
