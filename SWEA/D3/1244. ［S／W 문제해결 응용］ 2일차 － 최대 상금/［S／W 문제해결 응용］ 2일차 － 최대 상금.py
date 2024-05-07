def dfs(k):
    global num, c, ans
    if k == c:
        ans = max(ans, int("".join(num)))
        return
    for i in range(len(num)-1):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]
            if (k, int("".join(num))) not in visited:
                dfs(k + 1)
                visited.append((k, int("".join(num))))
            num[i], num[j] = num[j], num[i]
            
T = int(input())

for test_case in range(1, T + 1):
    n, c = input().split()
    c = int(c)
    num = []
    visited = []
    ans = 0
    
    for i in range(len(n)):
        num.append(n[i])
    
    dfs(0)
    
    print(f"#{test_case} {ans}")
    