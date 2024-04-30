import sys, re
input = sys.stdin.readline

tokens = re.findall(r'\d+|\D', input().strip())
numbers = []
operators = []

for token in tokens:
    if token.isdigit():
        numbers.append(int(token))
    else:
        operators.append(token)

ans = numbers[0]
i = 1
j = 0
while i < len(numbers):
    if operators[j] == '-':
        tmp = numbers[i]
        while j < len(operators) - 1 and operators[j + 1] == '+':
            i += 1
            j += 1
            tmp += numbers[i]
        ans -= tmp
    else:
        ans += numbers[i]
    i += 1
    j += 1

print(ans)