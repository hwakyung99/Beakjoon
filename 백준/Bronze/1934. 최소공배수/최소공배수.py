import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    ans = A * B // gcd(A, B)
    print(ans)
    