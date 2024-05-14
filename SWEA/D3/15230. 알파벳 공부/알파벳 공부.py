T = int(input())

for test_case in range(1, T + 1):
    arr = input().strip()
    s = 97
    cnt = 0
    for i in range(len(arr)):
        if arr[i] != chr(s):
            break
        cnt += 1
        s += 1
    
    print(f"#{test_case} {cnt}")
    