size = 100
for _ in range(1, 11):
    test_case = input()
    column = [0] * size
    diagonal_right, diagonal_left = 0, 0
    ans = 0
    
    for i in range(size):
        row = list(map(int, input().split()))
        ans = max(ans, sum(row))
        column = [column[j] + row[j] for j in range(size)]
        diagonal_right += row[i]
        diagonal_left += row[size-1-i]
    
    for c in column:
        ans = max(ans, c)

    ans = max(ans, diagonal_right, diagonal_left)
    
    print(f"#{test_case} {ans}")
        
    