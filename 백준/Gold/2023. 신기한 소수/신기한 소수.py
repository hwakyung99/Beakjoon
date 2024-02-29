import sys
import math
input = sys.stdin.readline


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def backtrack(n):
    if len(str(n)) == N:
        print(n)
        return
    for e in etc:
        c = n * 10 + e
        if is_prime(c):
            backtrack(c)


N = int(input())

first = [2, 3, 5, 7]
etc = [1, 3, 7, 9]

for f in first:
    backtrack(f)
