for test_case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    
    hight = [0] * 101
    for i in range(100):
        hight[arr[i]] += 1
    
    left, right = 1, 100
    while hight[left] == 0:
        left += 1
    while hight[right] == 0:
        right -= 1
        
    for _ in range(dump):
        if left + 1 >= right:
            break
        hight[left] -= 1
        hight[right] -= 1
        hight[left+1] += 1
        hight[right-1] += 1
        if hight[left] == 0:
            left += 1
        if hight[right] == 0:
            right -= 1
    
    print("#{0} {1}" .format(test_case, right-left))
        
