T = int(input())

for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    world = []
    tank = []
    for i in range(H):
        world.append(list(input().strip()))
        if not tank:
            for j in range(W):
                if world[i][j] in ['^', 'v', '<', '>']:
                    tank = [i, j]
                    break

    N = int(input())
    command = list(input().strip())

    for c in command:
        if c == 'U':
            if tank[0] > 0 and world[tank[0] - 1][tank[1]] == '.':
                world[tank[0]][tank[1]] = '.'
                tank[0] -= 1
            world[tank[0]][tank[1]] = '^'
        elif c == 'D':
            if tank[0] < H - 1 and world[tank[0] + 1][tank[1]] == '.':
                world[tank[0]][tank[1]] = '.'
                tank[0] += 1
            world[tank[0]][tank[1]] = 'v'
        elif c == 'L':
            if tank[1] > 0 and world[tank[0]][tank[1] - 1] == '.':
                world[tank[0]][tank[1]] = '.'
                tank[1] -= 1
            world[tank[0]][tank[1]] = '<'
        elif c == 'R':
            if tank[1] < W - 1 and world[tank[0]][tank[1] + 1] == '.':
                world[tank[0]][tank[1]] = '.'
                tank[1] += 1
            world[tank[0]][tank[1]] = '>'
        elif c == 'S':
            if world[tank[0]][tank[1]] == '^':
                for i in range(tank[0] - 1, -1, -1):
                    if world[i][tank[1]] == '*':
                        world[i][tank[1]] = '.'
                        break
                    elif world[i][tank[1]] == '#':
                        break
            elif world[tank[0]][tank[1]] == 'v':
                for i in range(tank[0] + 1, H):
                    if world[i][tank[1]] == '*':
                        world[i][tank[1]] = '.'
                        break
                    elif world[i][tank[1]] == '#':
                        break
            elif world[tank[0]][tank[1]] == '<':
                for i in range(tank[1] - 1, -1, -1):
                    if world[tank[0]][i] == '*':
                        world[tank[0]][i] = '.'
                        break
                    elif world[tank[0]][i] == '#':
                        break
            elif world[tank[0]][tank[1]] == '>':
                for i in range(tank[1] + 1, W):
                    if world[tank[0]][i] == '*':
                        world[tank[0]][i] = '.'
                        break
                    elif world[tank[0]][i] == '#':
                        break

    print(f"#{test_case}", end=" ")
    for i in range(H):
        print("".join(world[i]))
