import sys
from collections import deque

input = sys.stdin.readline

S, P = map(int, input().split())
DNA = input().strip()
A, C, G, T = map(int, input().split())
cnt = { 'A': 0, 'C': 0, 'G': 0, 'T': 0 }
ans = 0
d = deque()

for i in DNA:
    cnt[i] += 1
    d.append(i)
    if len(d) < P:
        continue
    elif len(d) == P:
        if cnt['A'] >= A and cnt['C'] >= C and cnt['G'] >= G and cnt['T'] >= T:
            ans += 1
        cnt[d.popleft()] -= 1


print(ans)
