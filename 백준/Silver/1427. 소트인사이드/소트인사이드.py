import sys
input = sys.stdin.readline

arr = sorted(input().strip(), reverse=True)
print(''.join(arr))
