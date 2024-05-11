T = int(input())

for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    visit = list(map(int, input().split()))
    visit.sort()
    ans = "Possible"

    b = 0  # 붕어빵 개수
    v = 0  # 손님 순서
    if visit[0] == 0:
        ans = "Impossible"
    else:
        for t in range(1, visit[-1] + 1):
            if t % m == 0:
                b += k
            while v <= len(visit) - 1 and t == visit[v]:
                if b == 0:
                    ans = "Impossible"
                    break
                else:
                    b -= 1
                    v += 1

    print(f"#{test_case} {ans}")
