T = int(input())

for test_case in range(1, T + 1):
    n = input().strip()
    max_num = int(n)
    min_num = int(n)

    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            tmp = n[:i] + n[j] + n[i + 1:j] + n[i] + n[j + 1:]
            if tmp[0] != '0':
                tmp = int("".join(tmp))
                max_num = max(max_num, tmp)
                min_num = min(min_num, tmp)

    print(f"#{test_case} {min_num} {max_num}")

