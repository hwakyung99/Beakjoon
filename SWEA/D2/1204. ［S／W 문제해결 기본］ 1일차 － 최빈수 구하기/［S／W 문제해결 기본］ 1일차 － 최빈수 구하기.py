T = int(input())

for test_case in range(1, T + 1):
    t = int(input())
    arr = list(map(int, input().split()))
    score = [0] * 101
    
    for i in arr:
        score[i] += 1

    ans = -1
    for i in range(101):
        if score[i] >= score[ans]:
            ans = i
    
    print(f"#{test_case} {ans}")
